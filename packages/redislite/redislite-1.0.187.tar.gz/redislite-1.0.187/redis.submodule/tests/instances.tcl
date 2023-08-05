# Multi-instance test framework.
# This is used in order to test Sentinel and Redis Cluster, and provides
# basic capabilities for spawning and handling N parallel Redis / Sentinel
# instances.
#
# Copyright (C) 2014 Salvatore Sanfilippo antirez@gmail.com
# This softare is released under the BSD License. See the COPYING file for
# more information.

package require Tcl 8.5

set tcl_precision 17
source ../support/redis.tcl
source ../support/util.tcl
source ../support/server.tcl
source ../support/test.tcl

set ::verbose 0
set ::pause_on_error 0
set ::simulate_error 0
set ::sentinel_instances {}
set ::redis_instances {}
set ::sentinel_base_port 20000
set ::redis_base_port 30000
set ::pids {} ; # We kill everything at exit
set ::dirs {} ; # We remove all the temp dirs at exit
set ::run_matching {} ; # If non empty, only tests matching pattern are run.

if {[catch {cd tmp}]} {
    puts "tmp directory not found."
    puts "Please run this test from the Redis source root."
    exit 1
}

# Spawn a redis or sentinel instance, depending on 'type'.
proc spawn_instance {type base_port count {conf {}}} {
    for {set j 0} {$j < $count} {incr j} {
        set port [find_available_port $base_port]
        incr base_port
        puts "Starting $type #$j at port $port"

        # Create a directory for this instance.
        set dirname "${type}_${j}"
        lappend ::dirs $dirname
        catch {exec rm -rf $dirname}
        file mkdir $dirname

        # Write the instance config file.
        set cfgfile [file join $dirname $type.conf]
        set cfg [open $cfgfile w]
        puts $cfg "port $port"
        puts $cfg "dir ./$dirname"
        puts $cfg "logfile log.txt"
        # Add additional config files
        foreach directive $conf {
            puts $cfg $directive
        }
        close $cfg

        # Finally exec it and remember the pid for later cleanup.
        if {$type eq "redis"} {
            set prgname redis-server
        } elseif {$type eq "sentinel"} {
            set prgname redis-sentinel
        } else {
            error "Unknown instance type."
        }
        set pid [exec ../../../src/${prgname} $cfgfile &]
        lappend ::pids $pid

        # Check availability
        if {[server_is_up 127.0.0.1 $port 100] == 0} {
            abort_sentinel_test "Problems starting $type #$j: ping timeout"
        }

        # Push the instance into the right list
        set link [redis 127.0.0.1 $port]
        $link reconnect 1
        lappend ::${type}_instances [list \
            pid $pid \
            host 127.0.0.1 \
            port $port \
            link $link \
        ]
    }
}

proc cleanup {} {
    puts "Cleaning up..."
    foreach pid $::pids {
        catch {exec kill -9 $pid}
    }
    foreach dir $::dirs {
        catch {exec rm -rf $dir}
    }
}

proc abort_sentinel_test msg {
    puts "WARNING: Aborting the test."
    puts ">>>>>>>> $msg"
    cleanup
    exit 1
}

proc parse_options {} {
    for {set j 0} {$j < [llength $::argv]} {incr j} {
        set opt [lindex $::argv $j]
        set val [lindex $::argv [expr $j+1]]
        if {$opt eq "--single"} {
            incr j
            set ::run_matching "*${val}*"
        } elseif {$opt eq "--pause-on-error"} {
            set ::pause_on_error 1
        } elseif {$opt eq "--fail"} {
            set ::simulate_error 1
        } elseif {$opt eq "--help"} {
            puts "Hello, I'm sentinel.tcl and I run Sentinel unit tests."
            puts "\nOptions:"
            puts "--single <pattern>      Only runs tests specified by pattern."
            puts "--pause-on-error        Pause for manual inspection on error."
            puts "--fail                  Simulate a test failure."
            puts "--help                  Shows this help."
            exit 0
        } else {
            puts "Unknown option $opt"
            exit 1
        }
    }
}

# If --pause-on-error option was passed at startup this function is called
# on error in order to give the developer a chance to understand more about
# the error condition while the instances are still running.
proc pause_on_error {} {
    puts ""
    puts [colorstr yellow "*** Please inspect the error now ***"]
    puts "\nType \"continue\" to resume the test, \"help\" for help screen.\n"
    while 1 {
        puts -nonewline "> "
        flush stdout
        set line [gets stdin]
        set argv [split $line " "]
        set cmd [lindex $argv 0]
        if {$cmd eq {continue}} {
            break
        } elseif {$cmd eq {show-redis-logs}} {
            set count 10
            if {[lindex $argv 1] ne {}} {set count [lindex $argv 1]}
            foreach_redis_id id {
                puts "=== REDIS $id ===="
                puts [exec tail -$count redis_$id/log.txt]
                puts "---------------------\n"
            }
        } elseif {$cmd eq {show-sentinel-logs}} {
            set count 10
            if {[lindex $argv 1] ne {}} {set count [lindex $argv 1]}
            foreach_sentinel_id id {
                puts "=== SENTINEL $id ===="
                puts [exec tail -$count sentinel_$id/log.txt]
                puts "---------------------\n"
            }
        } elseif {$cmd eq {ls}} {
            foreach_redis_id id {
                puts -nonewline "Redis $id"
                set errcode [catch {
                    set str {}
                    append str "@[RI $id tcp_port]: "
                    append str "[RI $id role] "
                    if {[RI $id role] eq {slave}} {
                        append str "[RI $id master_host]:[RI $id master_port]"
                    }
                    set str
                } retval]
                if {$errcode} {
                    puts " -- $retval"
                } else {
                    puts $retval
                }
            }
            foreach_sentinel_id id {
                puts -nonewline "Sentinel $id"
                set errcode [catch {
                    set str {}
                    append str "@[SI $id tcp_port]: "
                    append str "[join [S $id sentinel get-master-addr-by-name mymaster]]"
                    set str
                } retval]
                if {$errcode} {
                    puts " -- $retval"
                } else {
                    puts $retval
                }
            }
        } elseif {$cmd eq {help}} {
            puts "ls                     List Sentinel and Redis instances."
            puts "show-sentinel-logs \[N\] Show latest N lines of logs."
            puts "show-redis-logs \[N\]    Show latest N lines of logs."
            puts "S <id> cmd ... arg     Call command in Sentinel <id>."
            puts "R <id> cmd ... arg     Call command in Redis <id>."
            puts "SI <id> <field>        Show Sentinel <id> INFO <field>."
            puts "RI <id> <field>        Show Sentinel <id> INFO <field>."
            puts "continue               Resume test."
        } else {
            set errcode [catch {eval $line} retval]
            if {$retval ne {}} {puts "$retval"}
        }
    }
}

# We redefine 'test' as for Sentinel we don't use the server-client
# architecture for the test, everything is sequential.
proc test {descr code} {
    set ts [clock format [clock seconds] -format %H:%M:%S]
    puts -nonewline "$ts> $descr: "
    flush stdout

    if {[catch {set retval [uplevel 1 $code]} error]} {
        if {[string match "assertion:*" $error]} {
            set msg [string range $error 10 end]
            puts [colorstr red $msg]
            if {$::pause_on_error} pause_on_error
            puts "(Jumping to next unit after error)"
            return -code continue
        } else {
            # Re-raise, let handler up the stack take care of this.
            error $error $::errorInfo
        }
    } else {
        puts [colorstr green OK]
    }
}

proc run_tests {} {
    set tests [lsort [glob ../tests/*]]
    foreach test $tests {
        if {$::run_matching ne {} && [string match $::run_matching $test] == 0} {
            continue
        }
        if {[file isdirectory $test]} continue
        puts [colorstr yellow "Testing unit: [lindex [file split $test] end]"]
        source $test
    }
}

# The "S" command is used to interact with the N-th Sentinel.
# The general form is:
#
# S <sentinel-id> command arg arg arg ...
#
# Example to ping the Sentinel 0 (first instance): S 0 PING
proc S {n args} {
    set s [lindex $::sentinel_instances $n]
    [dict get $s link] {*}$args
}

# Like R but to chat with Redis instances.
proc R {n args} {
    set r [lindex $::redis_instances $n]
    [dict get $r link] {*}$args
}

proc get_info_field {info field} {
    set fl [string length $field]
    append field :
    foreach line [split $info "\n"] {
        set line [string trim $line "\r\n "]
        if {[string range $line 0 $fl] eq $field} {
            return [string range $line [expr {$fl+1}] end]
        }
    }
    return {}
}

proc SI {n field} {
    get_info_field [S $n info] $field
}

proc RI {n field} {
    get_info_field [R $n info] $field
}

# Iterate over IDs of sentinel or redis instances.
proc foreach_instance_id {instances idvar code} {
    upvar 1 $idvar id
    for {set id 0} {$id < [llength $instances]} {incr id} {
        set errcode [catch {uplevel 1 $code} result]
        if {$errcode == 1} {
            error $result $::errorInfo $::errorCode
        } elseif {$errcode == 4} {
            continue
        } elseif {$errcode == 3} {
            break
        } elseif {$errcode != 0} {
            return -code $errcode $result
        }
    }
}

proc foreach_sentinel_id {idvar code} {
    set errcode [catch {uplevel 1 [list foreach_instance_id $::sentinel_instances $idvar $code]} result]
    return -code $errcode $result
}

proc foreach_redis_id {idvar code} {
    set errcode [catch {uplevel 1 [list foreach_instance_id $::redis_instances $idvar $code]} result]
    return -code $errcode $result
}

# Get the specific attribute of the specified instance type, id.
proc get_instance_attrib {type id attrib} {
    dict get [lindex [set ::${type}_instances] $id] $attrib
}

# Set the specific attribute of the specified instance type, id.
proc set_instance_attrib {type id attrib newval} {
    set d [lindex [set ::${type}_instances] $id]
    dict set d $attrib $newval
    lset ::${type}_instances $id $d
}

# Create a master-slave cluster of the given number of total instances.
# The first instance "0" is the master, all others are configured as
# slaves.
proc create_redis_master_slave_cluster n {
    foreach_redis_id id {
        if {$id == 0} {
            # Our master.
            R $id slaveof no one
            R $id flushall
        } elseif {$id < $n} {
            R $id slaveof [get_instance_attrib redis 0 host] \
                          [get_instance_attrib redis 0 port]
        } else {
            # Instances not part of the cluster.
            R $id slaveof no one
        }
    }
    # Wait for all the slaves to sync.
    wait_for_condition 1000 50 {
        [RI 0 connected_slaves] == ($n-1)
    } else {
        fail "Unable to create a master-slaves cluster."
    }
}

proc get_instance_id_by_port {type port} {
    foreach_${type}_id id {
        if {[get_instance_attrib $type $id port] == $port} {
            return $id
        }
    }
    fail "Instance $type port $port not found."
}

# Kill an instance of the specified type/id with SIGKILL.
# This function will mark the instance PID as -1 to remember that this instance
# is no longer running and will remove its PID from the list of pids that
# we kill at cleanup.
#
# The instance can be restarted with restart-instance.
proc kill_instance {type id} {
    set pid [get_instance_attrib $type $id pid]
    if {$pid == -1} {
        error "You tried to kill $type $id twice."
    }
    exec kill -9 $pid
    set_instance_attrib $type $id pid -1
    set_instance_attrib $type $id link you_tried_to_talk_with_killed_instance

    # Remove the PID from the list of pids to kill at exit.
    set ::pids [lsearch -all -inline -not -exact $::pids $pid]
}

# Return true of the instance of the specified type/id is killed.
proc instance_is_killed {type id} {
    set pid [get_instance_attrib $type $id pid]
    expr {$pid == -1}
}

# Restart an instance previously killed by kill_instance
proc restart_instance {type id} {
    set dirname "${type}_${id}"
    set cfgfile [file join $dirname $type.conf]
    set port [get_instance_attrib $type $id port]

    # Execute the instance with its old setup and append the new pid
    # file for cleanup.
    if {$type eq "redis"} {
        set prgname redis-server
    } else {
        set prgname redis-sentinel
    }
    set pid [exec ../../../src/${prgname} $cfgfile &]
    set_instance_attrib $type $id pid $pid
    lappend ::pids $pid

    # Check that the instance is running
    if {[server_is_up 127.0.0.1 $port 100] == 0} {
        abort_sentinel_test "Problems starting $type #$id: ping timeout"
    }

    # Connect with it with a fresh link
    set link [redis 127.0.0.1 $port]
    $link reconnect 1
    set_instance_attrib $type $id link $link
}


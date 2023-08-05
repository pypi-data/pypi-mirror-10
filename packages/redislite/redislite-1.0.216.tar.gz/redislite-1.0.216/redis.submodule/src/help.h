/* Automatically generated by utils/generate-command-help.rb, do not edit. */

#ifndef __REDIS_HELP_H
#define __REDIS_HELP_H

static char *commandGroups[] = {
    "generic",
    "string",
    "list",
    "set",
    "sorted_set",
    "hash",
    "pubsub",
    "transactions",
    "connection",
    "server",
    "scripting",
    "hyperloglog"
};

struct commandHelp {
  char *name;
  char *params;
  char *summary;
  int group;
  char *since;
} commandHelp[] = {
    { "APPEND",
    "key value",
    "Append a value to a key",
    1,
    "2.0.0" },
    { "AUTH",
    "password",
    "Authenticate to the server",
    8,
    "1.0.0" },
    { "BGREWRITEAOF",
    "-",
    "Asynchronously rewrite the append-only file",
    9,
    "1.0.0" },
    { "BGSAVE",
    "-",
    "Asynchronously save the dataset to disk",
    9,
    "1.0.0" },
    { "BITCOUNT",
    "key [start] [end]",
    "Count set bits in a string",
    1,
    "2.6.0" },
    { "BITOP",
    "operation destkey key [key ...]",
    "Perform bitwise operations between strings",
    1,
    "2.6.0" },
    { "BITPOS",
    "key bit [start] [end]",
    "Find first bit set or clear in a string",
    1,
    "2.8.7" },
    { "BLPOP",
    "key [key ...] timeout",
    "Remove and get the first element in a list, or block until one is available",
    2,
    "2.0.0" },
    { "BRPOP",
    "key [key ...] timeout",
    "Remove and get the last element in a list, or block until one is available",
    2,
    "2.0.0" },
    { "BRPOPLPUSH",
    "source destination timeout",
    "Pop a value from a list, push it to another list and return it; or block until one is available",
    2,
    "2.2.0" },
    { "CLIENT GETNAME",
    "-",
    "Get the current connection name",
    9,
    "2.6.9" },
    { "CLIENT KILL",
    "ip:port",
    "Kill the connection of a client",
    9,
    "2.4.0" },
    { "CLIENT LIST",
    "-",
    "Get the list of client connections",
    9,
    "2.4.0" },
    { "CLIENT PAUSE",
    "timeout",
    "Stop processing commands from clients for some time",
    9,
    "2.9.50" },
    { "CLIENT SETNAME",
    "connection-name",
    "Set the current connection name",
    9,
    "2.6.9" },
    { "CONFIG GET",
    "parameter",
    "Get the value of a configuration parameter",
    9,
    "2.0.0" },
    { "CONFIG RESETSTAT",
    "-",
    "Reset the stats returned by INFO",
    9,
    "2.0.0" },
    { "CONFIG REWRITE",
    "-",
    "Rewrite the configuration file with the in memory configuration",
    9,
    "2.8.0" },
    { "CONFIG SET",
    "parameter value",
    "Set a configuration parameter to the given value",
    9,
    "2.0.0" },
    { "DBSIZE",
    "-",
    "Return the number of keys in the selected database",
    9,
    "1.0.0" },
    { "DEBUG OBJECT",
    "key",
    "Get debugging information about a key",
    9,
    "1.0.0" },
    { "DEBUG SEGFAULT",
    "-",
    "Make the server crash",
    9,
    "1.0.0" },
    { "DECR",
    "key",
    "Decrement the integer value of a key by one",
    1,
    "1.0.0" },
    { "DECRBY",
    "key decrement",
    "Decrement the integer value of a key by the given number",
    1,
    "1.0.0" },
    { "DEL",
    "key [key ...]",
    "Delete a key",
    0,
    "1.0.0" },
    { "DISCARD",
    "-",
    "Discard all commands issued after MULTI",
    7,
    "2.0.0" },
    { "DUMP",
    "key",
    "Return a serialized version of the value stored at the specified key.",
    0,
    "2.6.0" },
    { "ECHO",
    "message",
    "Echo the given string",
    8,
    "1.0.0" },
    { "EVAL",
    "script numkeys key [key ...] arg [arg ...]",
    "Execute a Lua script server side",
    10,
    "2.6.0" },
    { "EVALSHA",
    "sha1 numkeys key [key ...] arg [arg ...]",
    "Execute a Lua script server side",
    10,
    "2.6.0" },
    { "EXEC",
    "-",
    "Execute all commands issued after MULTI",
    7,
    "1.2.0" },
    { "EXISTS",
    "key",
    "Determine if a key exists",
    0,
    "1.0.0" },
    { "EXPIRE",
    "key seconds",
    "Set a key's time to live in seconds",
    0,
    "1.0.0" },
    { "EXPIREAT",
    "key timestamp",
    "Set the expiration for a key as a UNIX timestamp",
    0,
    "1.2.0" },
    { "FLUSHALL",
    "-",
    "Remove all keys from all databases",
    9,
    "1.0.0" },
    { "FLUSHDB",
    "-",
    "Remove all keys from the current database",
    9,
    "1.0.0" },
    { "GET",
    "key",
    "Get the value of a key",
    1,
    "1.0.0" },
    { "GETBIT",
    "key offset",
    "Returns the bit value at offset in the string value stored at key",
    1,
    "2.2.0" },
    { "GETRANGE",
    "key start end",
    "Get a substring of the string stored at a key",
    1,
    "2.4.0" },
    { "GETSET",
    "key value",
    "Set the string value of a key and return its old value",
    1,
    "1.0.0" },
    { "HDEL",
    "key field [field ...]",
    "Delete one or more hash fields",
    5,
    "2.0.0" },
    { "HEXISTS",
    "key field",
    "Determine if a hash field exists",
    5,
    "2.0.0" },
    { "HGET",
    "key field",
    "Get the value of a hash field",
    5,
    "2.0.0" },
    { "HGETALL",
    "key",
    "Get all the fields and values in a hash",
    5,
    "2.0.0" },
    { "HINCRBY",
    "key field increment",
    "Increment the integer value of a hash field by the given number",
    5,
    "2.0.0" },
    { "HINCRBYFLOAT",
    "key field increment",
    "Increment the float value of a hash field by the given amount",
    5,
    "2.6.0" },
    { "HKEYS",
    "key",
    "Get all the fields in a hash",
    5,
    "2.0.0" },
    { "HLEN",
    "key",
    "Get the number of fields in a hash",
    5,
    "2.0.0" },
    { "HMGET",
    "key field [field ...]",
    "Get the values of all the given hash fields",
    5,
    "2.0.0" },
    { "HMSET",
    "key field value [field value ...]",
    "Set multiple hash fields to multiple values",
    5,
    "2.0.0" },
    { "HSCAN",
    "key cursor [MATCH pattern] [COUNT count]",
    "Incrementally iterate hash fields and associated values",
    5,
    "2.8.0" },
    { "HSET",
    "key field value",
    "Set the string value of a hash field",
    5,
    "2.0.0" },
    { "HSETNX",
    "key field value",
    "Set the value of a hash field, only if the field does not exist",
    5,
    "2.0.0" },
    { "HVALS",
    "key",
    "Get all the values in a hash",
    5,
    "2.0.0" },
    { "INCR",
    "key",
    "Increment the integer value of a key by one",
    1,
    "1.0.0" },
    { "INCRBY",
    "key increment",
    "Increment the integer value of a key by the given amount",
    1,
    "1.0.0" },
    { "INCRBYFLOAT",
    "key increment",
    "Increment the float value of a key by the given amount",
    1,
    "2.6.0" },
    { "INFO",
    "[section]",
    "Get information and statistics about the server",
    9,
    "1.0.0" },
    { "KEYS",
    "pattern",
    "Find all keys matching the given pattern",
    0,
    "1.0.0" },
    { "LASTSAVE",
    "-",
    "Get the UNIX time stamp of the last successful save to disk",
    9,
    "1.0.0" },
    { "LINDEX",
    "key index",
    "Get an element from a list by its index",
    2,
    "1.0.0" },
    { "LINSERT",
    "key BEFORE|AFTER pivot value",
    "Insert an element before or after another element in a list",
    2,
    "2.2.0" },
    { "LLEN",
    "key",
    "Get the length of a list",
    2,
    "1.0.0" },
    { "LPOP",
    "key",
    "Remove and get the first element in a list",
    2,
    "1.0.0" },
    { "LPUSH",
    "key value [value ...]",
    "Prepend one or multiple values to a list",
    2,
    "1.0.0" },
    { "LPUSHX",
    "key value",
    "Prepend a value to a list, only if the list exists",
    2,
    "2.2.0" },
    { "LRANGE",
    "key start stop",
    "Get a range of elements from a list",
    2,
    "1.0.0" },
    { "LREM",
    "key count value",
    "Remove elements from a list",
    2,
    "1.0.0" },
    { "LSET",
    "key index value",
    "Set the value of an element in a list by its index",
    2,
    "1.0.0" },
    { "LTRIM",
    "key start stop",
    "Trim a list to the specified range",
    2,
    "1.0.0" },
    { "MGET",
    "key [key ...]",
    "Get the values of all the given keys",
    1,
    "1.0.0" },
    { "MIGRATE",
    "host port key destination-db timeout [COPY] [REPLACE]",
    "Atomically transfer a key from a Redis instance to another one.",
    0,
    "2.6.0" },
    { "MONITOR",
    "-",
    "Listen for all requests received by the server in real time",
    9,
    "1.0.0" },
    { "MOVE",
    "key db",
    "Move a key to another database",
    0,
    "1.0.0" },
    { "MSET",
    "key value [key value ...]",
    "Set multiple keys to multiple values",
    1,
    "1.0.1" },
    { "MSETNX",
    "key value [key value ...]",
    "Set multiple keys to multiple values, only if none of the keys exist",
    1,
    "1.0.1" },
    { "MULTI",
    "-",
    "Mark the start of a transaction block",
    7,
    "1.2.0" },
    { "OBJECT",
    "subcommand [arguments [arguments ...]]",
    "Inspect the internals of Redis objects",
    0,
    "2.2.3" },
    { "PERSIST",
    "key",
    "Remove the expiration from a key",
    0,
    "2.2.0" },
    { "PEXPIRE",
    "key milliseconds",
    "Set a key's time to live in milliseconds",
    0,
    "2.6.0" },
    { "PEXPIREAT",
    "key milliseconds-timestamp",
    "Set the expiration for a key as a UNIX timestamp specified in milliseconds",
    0,
    "2.6.0" },
    { "PFADD",
    "key element [element ...]",
    "Adds the specified elements to the specified HyperLogLog.",
    11,
    "2.8.9" },
    { "PFCOUNT",
    "key [key ...]",
    "Return the approximated cardinality of the set(s) observed by the HyperLogLog at key(s).",
    11,
    "2.8.9" },
    { "PFMERGE",
    "destkey sourcekey [sourcekey ...]",
    "Merge N different HyperLogLogs into a single one.",
    11,
    "2.8.9" },
    { "PING",
    "-",
    "Ping the server",
    8,
    "1.0.0" },
    { "PSETEX",
    "key milliseconds value",
    "Set the value and expiration in milliseconds of a key",
    1,
    "2.6.0" },
    { "PSUBSCRIBE",
    "pattern [pattern ...]",
    "Listen for messages published to channels matching the given patterns",
    6,
    "2.0.0" },
    { "PTTL",
    "key",
    "Get the time to live for a key in milliseconds",
    0,
    "2.6.0" },
    { "PUBLISH",
    "channel message",
    "Post a message to a channel",
    6,
    "2.0.0" },
    { "PUBSUB",
    "subcommand [argument [argument ...]]",
    "Inspect the state of the Pub/Sub subsystem",
    6,
    "2.8.0" },
    { "PUNSUBSCRIBE",
    "[pattern [pattern ...]]",
    "Stop listening for messages posted to channels matching the given patterns",
    6,
    "2.0.0" },
    { "QUIT",
    "-",
    "Close the connection",
    8,
    "1.0.0" },
    { "RANDOMKEY",
    "-",
    "Return a random key from the keyspace",
    0,
    "1.0.0" },
    { "RENAME",
    "key newkey",
    "Rename a key",
    0,
    "1.0.0" },
    { "RENAMENX",
    "key newkey",
    "Rename a key, only if the new key does not exist",
    0,
    "1.0.0" },
    { "RESTORE",
    "key ttl serialized-value",
    "Create a key using the provided serialized value, previously obtained using DUMP.",
    0,
    "2.6.0" },
    { "RPOP",
    "key",
    "Remove and get the last element in a list",
    2,
    "1.0.0" },
    { "RPOPLPUSH",
    "source destination",
    "Remove the last element in a list, append it to another list and return it",
    2,
    "1.2.0" },
    { "RPUSH",
    "key value [value ...]",
    "Append one or multiple values to a list",
    2,
    "1.0.0" },
    { "RPUSHX",
    "key value",
    "Append a value to a list, only if the list exists",
    2,
    "2.2.0" },
    { "SADD",
    "key member [member ...]",
    "Add one or more members to a set",
    3,
    "1.0.0" },
    { "SAVE",
    "-",
    "Synchronously save the dataset to disk",
    9,
    "1.0.0" },
    { "SCAN",
    "cursor [MATCH pattern] [COUNT count]",
    "Incrementally iterate the keys space",
    0,
    "2.8.0" },
    { "SCARD",
    "key",
    "Get the number of members in a set",
    3,
    "1.0.0" },
    { "SCRIPT EXISTS",
    "script [script ...]",
    "Check existence of scripts in the script cache.",
    10,
    "2.6.0" },
    { "SCRIPT FLUSH",
    "-",
    "Remove all the scripts from the script cache.",
    10,
    "2.6.0" },
    { "SCRIPT KILL",
    "-",
    "Kill the script currently in execution.",
    10,
    "2.6.0" },
    { "SCRIPT LOAD",
    "script",
    "Load the specified Lua script into the script cache.",
    10,
    "2.6.0" },
    { "SDIFF",
    "key [key ...]",
    "Subtract multiple sets",
    3,
    "1.0.0" },
    { "SDIFFSTORE",
    "destination key [key ...]",
    "Subtract multiple sets and store the resulting set in a key",
    3,
    "1.0.0" },
    { "SELECT",
    "index",
    "Change the selected database for the current connection",
    8,
    "1.0.0" },
    { "SET",
    "key value [EX seconds] [PX milliseconds] [NX|XX]",
    "Set the string value of a key",
    1,
    "1.0.0" },
    { "SETBIT",
    "key offset value",
    "Sets or clears the bit at offset in the string value stored at key",
    1,
    "2.2.0" },
    { "SETEX",
    "key seconds value",
    "Set the value and expiration of a key",
    1,
    "2.0.0" },
    { "SETNX",
    "key value",
    "Set the value of a key, only if the key does not exist",
    1,
    "1.0.0" },
    { "SETRANGE",
    "key offset value",
    "Overwrite part of a string at key starting at the specified offset",
    1,
    "2.2.0" },
    { "SHUTDOWN",
    "[NOSAVE] [SAVE]",
    "Synchronously save the dataset to disk and then shut down the server",
    9,
    "1.0.0" },
    { "SINTER",
    "key [key ...]",
    "Intersect multiple sets",
    3,
    "1.0.0" },
    { "SINTERSTORE",
    "destination key [key ...]",
    "Intersect multiple sets and store the resulting set in a key",
    3,
    "1.0.0" },
    { "SISMEMBER",
    "key member",
    "Determine if a given value is a member of a set",
    3,
    "1.0.0" },
    { "SLAVEOF",
    "host port",
    "Make the server a slave of another instance, or promote it as master",
    9,
    "1.0.0" },
    { "SLOWLOG",
    "subcommand [argument]",
    "Manages the Redis slow queries log",
    9,
    "2.2.12" },
    { "SMEMBERS",
    "key",
    "Get all the members in a set",
    3,
    "1.0.0" },
    { "SMOVE",
    "source destination member",
    "Move a member from one set to another",
    3,
    "1.0.0" },
    { "SORT",
    "key [BY pattern] [LIMIT offset count] [GET pattern [GET pattern ...]] [ASC|DESC] [ALPHA] [STORE destination]",
    "Sort the elements in a list, set or sorted set",
    0,
    "1.0.0" },
    { "SPOP",
    "key",
    "Remove and return a random member from a set",
    3,
    "1.0.0" },
    { "SRANDMEMBER",
    "key [count]",
    "Get one or multiple random members from a set",
    3,
    "1.0.0" },
    { "SREM",
    "key member [member ...]",
    "Remove one or more members from a set",
    3,
    "1.0.0" },
    { "SSCAN",
    "key cursor [MATCH pattern] [COUNT count]",
    "Incrementally iterate Set elements",
    3,
    "2.8.0" },
    { "STRLEN",
    "key",
    "Get the length of the value stored in a key",
    1,
    "2.2.0" },
    { "SUBSCRIBE",
    "channel [channel ...]",
    "Listen for messages published to the given channels",
    6,
    "2.0.0" },
    { "SUNION",
    "key [key ...]",
    "Add multiple sets",
    3,
    "1.0.0" },
    { "SUNIONSTORE",
    "destination key [key ...]",
    "Add multiple sets and store the resulting set in a key",
    3,
    "1.0.0" },
    { "SYNC",
    "-",
    "Internal command used for replication",
    9,
    "1.0.0" },
    { "TIME",
    "-",
    "Return the current server time",
    9,
    "2.6.0" },
    { "TTL",
    "key",
    "Get the time to live for a key",
    0,
    "1.0.0" },
    { "TYPE",
    "key",
    "Determine the type stored at key",
    0,
    "1.0.0" },
    { "UNSUBSCRIBE",
    "[channel [channel ...]]",
    "Stop listening for messages posted to the given channels",
    6,
    "2.0.0" },
    { "UNWATCH",
    "-",
    "Forget about all watched keys",
    7,
    "2.2.0" },
    { "WATCH",
    "key [key ...]",
    "Watch the given keys to determine execution of the MULTI/EXEC block",
    7,
    "2.2.0" },
    { "ZADD",
    "key score member [score member ...]",
    "Add one or more members to a sorted set, or update its score if it already exists",
    4,
    "1.2.0" },
    { "ZCARD",
    "key",
    "Get the number of members in a sorted set",
    4,
    "1.2.0" },
    { "ZCOUNT",
    "key min max",
    "Count the members in a sorted set with scores within the given values",
    4,
    "2.0.0" },
    { "ZINCRBY",
    "key increment member",
    "Increment the score of a member in a sorted set",
    4,
    "1.2.0" },
    { "ZINTERSTORE",
    "destination numkeys key [key ...] [WEIGHTS weight] [AGGREGATE SUM|MIN|MAX]",
    "Intersect multiple sorted sets and store the resulting sorted set in a new key",
    4,
    "2.0.0" },
    { "ZLEXCOUNT",
    "key min max",
    "Count the number of members in a sorted set between a given lexicographical range",
    4,
    "2.8.9" },
    { "ZRANGE",
    "key start stop [WITHSCORES]",
    "Return a range of members in a sorted set, by index",
    4,
    "1.2.0" },
    { "ZRANGEBYLEX",
    "key min max [LIMIT offset count]",
    "Return a range of members in a sorted set, by lexicographical range",
    4,
    "2.8.9" },
    { "ZRANGEBYSCORE",
    "key min max [WITHSCORES] [LIMIT offset count]",
    "Return a range of members in a sorted set, by score",
    4,
    "1.0.5" },
    { "ZRANK",
    "key member",
    "Determine the index of a member in a sorted set",
    4,
    "2.0.0" },
    { "ZREM",
    "key member [member ...]",
    "Remove one or more members from a sorted set",
    4,
    "1.2.0" },
    { "ZREMRANGEBYLEX",
    "key min max",
    "Remove all members in a sorted set between the given lexicographical range",
    4,
    "2.8.9" },
    { "ZREMRANGEBYRANK",
    "key start stop",
    "Remove all members in a sorted set within the given indexes",
    4,
    "2.0.0" },
    { "ZREMRANGEBYSCORE",
    "key min max",
    "Remove all members in a sorted set within the given scores",
    4,
    "1.2.0" },
    { "ZREVRANGE",
    "key start stop [WITHSCORES]",
    "Return a range of members in a sorted set, by index, with scores ordered from high to low",
    4,
    "1.2.0" },
    { "ZREVRANGEBYSCORE",
    "key max min [WITHSCORES] [LIMIT offset count]",
    "Return a range of members in a sorted set, by score, with scores ordered from high to low",
    4,
    "2.2.0" },
    { "ZREVRANK",
    "key member",
    "Determine the index of a member in a sorted set, with scores ordered from high to low",
    4,
    "2.0.0" },
    { "ZSCAN",
    "key cursor [MATCH pattern] [COUNT count]",
    "Incrementally iterate sorted sets elements and associated scores",
    4,
    "2.8.0" },
    { "ZSCORE",
    "key member",
    "Get the score associated with the given member in a sorted set",
    4,
    "1.2.0" },
    { "ZUNIONSTORE",
    "destination numkeys key [key ...] [WEIGHTS weight] [AGGREGATE SUM|MIN|MAX]",
    "Add multiple sorted sets and store the resulting sorted set in a new key",
    4,
    "2.0.0" }
};

#endif

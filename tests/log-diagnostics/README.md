# Log sync diagnostics

Host regressions for the module log-capture path:

```sh
python3 tests/log-diagnostics/run.py
python3 tests/logcat-import/run.py
```

The first check compiles the production diagnostic writer against Android/DAO
stubs and executes it with no ordinary `AndroidLog` implementation on the
classpath. It covers root denial/exception/recovery, deduplication, environment
identity, database-failure fallback without recursion, and diagnostic records
surviving refresh/export SQL.

The second check executes the production LSPosed log-copy script against
disposable directories. It covers the direct, `/proc/1/root` and both `nsenter`
source-access strategies, empty/success/copy-denied/chmod-denied/source-missing
results, and asserts that a failed staging copy leaves the previous target
contents untouched.

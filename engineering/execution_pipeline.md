# Execution Pipeline

## Purpose

This document defines the end-to-end execution flow for OpenSceneFORCE
V7 operations.

The execution pipeline controls how the application performs:

-   Backup
-   Restore
-   Repair
-   Update
-   Safe Mode

The goal is to make every operation predictable, logged, validated, and
safe.

------------------------------------------------------------------------

## Core Rule

Every operation must follow this order:

``` text
Request → Validate → Execute → Log → Report Result
```

No operation should run directly from the UI without passing through the
orchestrator.

------------------------------------------------------------------------

## Main Execution Flow

``` text
User Action
   ↓
UI Layer
   ↓
Orchestrator
   ↓
Safety Check
   ↓
State Update
   ↓
Core Engine
   ↓
Service Layer
   ↓
Logger
   ↓
Result Returned to UI
```

------------------------------------------------------------------------

## Backup Flow

``` text
Start Backup
 ↓
Validate OBS paths
 ↓
Validate backup destination
 ↓
Create backup folder
 ↓
Copy OBS scenes, profiles, and settings
 ↓
Verify copied files
 ↓
Write backup log
 ↓
Return success or failure
```

Required module:

`app/core/backup_engine.py`

------------------------------------------------------------------------

## Restore Flow

``` text
Start Restore
 ↓
Validate selected backup
 ↓
Confirm backup contains required data
 ↓
Create safety checkpoint
 ↓
Restore files
 ↓
Validate restored OBS structure
 ↓
Write restore log
 ↓
Return success or failure
```

Required module:

`app/core/restore_engine.py`

------------------------------------------------------------------------

## Repair Flow

``` text
Start Repair
 ↓
Run system check
 ↓
Detect missing folders or broken paths
 ↓
Repair safe items
 ↓
Skip dangerous changes
 ↓
Write repair report
 ↓
Return repair result
```

Required module:

`app/core/repair_engine.py`

------------------------------------------------------------------------

## Update Flow

``` text
Start Update
 ↓
Check current version
 ↓
Check available version
 ↓
Validate update source
 ↓
Create pre-update checkpoint
 ↓
Apply update
 ↓
Verify updated files
 ↓
Write update log
 ↓
Return update result
```

Required modules:

-   `app/core/update_engine.py`
-   `app/services/github_update_service.py`
-   `app/services/version_service.py`

------------------------------------------------------------------------

## Safe Mode Flow

``` text
Start Operation
 ↓
Run system safety check
 ↓
If unsafe state detected
 ↓
Block risky operation
 ↓
Set system state to SAFE_MODE
 ↓
Allow repair or recovery only
```

Required module:

`app/safety/system_check.py`

------------------------------------------------------------------------

## Logging Requirement

Every operation must log:

-   Operation name
-   Start time
-   End time
-   Result
-   Error message if failed
-   Recovery suggestion if needed

Required module:

`app/utils/logger.py`

------------------------------------------------------------------------

## Pipeline Status Values

-   PENDING
-   RUNNING
-   SUCCESS
-   FAILED
-   WARNING
-   SAFE_MODE
-   CANCELLED

------------------------------------------------------------------------

## Final Rule

The UI should never perform heavy logic directly.

-   The UI asks.
-   The orchestrator controls.
-   The engines execute.
-   The logger records.
-   The state machine tracks the lifecycle.

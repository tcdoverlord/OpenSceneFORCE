# OpenSceneFORCE V7

![OpenSceneFORCE
Banner](engineering/assets/banners/opensceneforce_v7_readme_banner.png)

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![PySide6](https://img.shields.io/badge/PySide6-Qt%20for%20Python-41CD52?logo=qt&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%2010%20%7C%2011-0078D6?logo=windows)
![Status](https://img.shields.io/badge/Status-Foundation%20Scaffold-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

OpenSceneFORCE V7 is a desktop application designed to safely manage the
complete lifecycle of OBS Studio. Rather than acting as a simple backup
utility, it provides a controlled execution platform for backing up,
restoring, repairing, updating, and safely launching OBS through a
routed, safety-gated architecture. Every operation is validated before
execution, logged for traceability, and designed to protect existing OBS
configurations from accidental loss or corruption.

The project follows a modular Python architecture built with
**PySide6**, where the user interface communicates only with a central
Orchestrator. The Orchestrator validates requests through the Safety
Layer before dispatching them to specialized engines responsible for
backup, restore, repair, updates, and system control.

------------------------------------------------------------------------

## 📚 Documentation

Whether you're using OpenSceneFORCE or contributing to its development, the following documents provide a deeper look into the project.

| Document | Description |
|----------|-------------|
| [Architecture](engineering/architecture.md) | Complete system architecture, execution pipeline, engineering philosophy, and repository structure. |
| [Execution Pipeline](engineering/execution_pipeline.md) | End-to-end execution flow for backup, restore, repair, update, and Safe Mode operations. |
| [State Machine](engineering/state_machine.md) | Runtime states, transitions, validation gates, and execution lifecycle. |
| [Coding Standards](engineering/coding_standards.md) | Project conventions, naming standards, logging requirements, and development guidelines. |

------------------------------------------------------------------------

## Planned Features

-   Run OBS In Safe Mode
-   Create portable OBS backups
-   Restore OBS configurations
-   Repair OBS installations
-   Update OpenSceneFORCE
-   USB-first backup workflow
-   Automatic restore points
-   Timestamped operation and error logs
-   Version compatibility checks
-   Modular PySide6 desktop interface

------------------------------------------------------------------------

## Architecture

The project follows an Architecture as Code philosophy.

    GUI
     ↓
    Orchestrator
     ↓
    Safety Layer
     ↓
    Core Engines
     ↓
    Services + System
     ↓
    OBS Studio
     ↓
    Storage + Logs + State

Detailed documentation:

-   `engineering/architecture.md`
-   `engineering/execution_pipeline.md`
-   `engineering/state_machine.md`

------------------------------------------------------------------------

## Project Structure

``` text
app/            Application source
docs/           Product documentation
engineering/    Architecture and design
tools/          Developer utilities
```

------------------------------------------------------------------------

## Current Status

**Foundation Scaffold Complete**

The project structure, execution pipeline, documentation, and
engineering standards have been established. The next phase focuses on
implementing the production engines that power Safe Mode, Backup,
Restore, Repair, and Update workflows.

------------------------------------------------------------------------

## Requirements

-   Python 3.11+
-   PySide6
-   Windows 10 or Windows 11

Install dependencies:

``` powershell
python tools/install_deps.py
```

------------------------------------------------------------------------

## Engineering Philosophy

OpenSceneFORCE is designed as a maintainable software platform---not a
collection of scripts. Architecture, documentation, and implementation
evolve together so the project remains scalable, testable, and easy to
contribute to.

> **Architecture drives implementation---not the other way around.**

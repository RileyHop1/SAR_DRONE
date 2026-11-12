# SAR Drone Documentation

## Introduction

JDR is developing an autonomous search-and-rescue drone as a senior engineering project. Our goal is to help search teams survey difficult terrain and identify locations worth investigating. The prototype combines a reviewed search route, RGB and thermal observations, estimated candidate locations, and evidence for human assessment.

The intended workflow starts with an operator defining a search area, reviewing the route, and authorizing launch. During the supervised mission, the drone follows the planned route and flags possible people. It sends status and candidate-location updates when communications permit and retains imagery and records for later review. The mission concludes with return or an appropriate recovery response.

This overview draws on the team's product requirements, design specification, and master test plan. They describe a prototype under development with performance targets and acceptance decisions still to resolve.

## Project goals

- Execute an operator-approved search and record progress against the planned route.
- Use RGB and thermal observations to identify possible people.
- Associate candidate observations with estimated coordinates, timestamps, and reviewable evidence.
- Provide concise updates when connected and retain records through communication outages.
- Support operator intervention and defined return, low-energy, lost-link, and navigation-failure responses.
- Demonstrate the complete workflow with reproducible tests and documented limitations.

Detection performance, location error, endurance, and operating limits require agreed acceptance criteria and measured evidence. Adaptive mission planning is a stretch goal. The source drafts also classify in-flight image transmission as stretch work; its priority needs reconciliation with the team's newer video-link design discussions.

## System at a glance

The current software planning uses three onboard computers.

| Computer | Planned responsibility |
| --- | --- |
| Raspberry Pi | ROS 2 Jazzy mission management and coordination |
| Jetson Orin Nano Super | RGB and thermal processing and candidate detections |
| Pixhawk 6C Mini | PX4 flight control running on NuttX |

Laptop development and Gazebo simulation support testing before hardware integration. Current component choices and software planning appear in the [software roadmap](software-roadmap.md). The earlier design specification establishes broader mission, sensing, evidence, communications, and operator-interface responsibilities, with hardware selections still provisional in that document.

Validation will progress through software and simulation checks, bench integration, and authorized supervised flight. Test records should identify the configuration, expected behavior, actual results, and supporting evidence. The master test plan covers nominal missions and failures such as communication loss, low energy, and uncertain navigation.

## Start here

New to the project? Follow [Setting Up Your Environment](environment/README.md) to prepare your development machine.

1. Read the introduction above and the [repository README](https://github.com/RileyHop1/SAR_DRONE) for the project and code layout.
2. Read the [software roadmap](software-roadmap.md) for goals, current work, and open decisions.
3. Follow the [Git conventions](git-conventions.md) for branches, commits, and pull requests.
4. Follow the [software development conventions](software-development-conventions.md) for interface documentation, tests, implementation, and review.
5. Follow the conventions for the language you are writing. [C++](cpp-conventions.md) · [Python](python-conventions.md)

## Proposed website sections

This is a provisional navigation structure for team review. Entries marked planned describe pages to develop.

| Section | What readers should find | Current material |
| --- | --- | --- |
| Project overview | Purpose, goals, scope, operator workflow, and project status | This home page |
| Getting started | Required tools, local setup, container builds, first ROS run, and troubleshooting | [Environment setup](environment/README.md) |
| Architecture and interfaces | System diagram, computer responsibilities, package structure, message definitions, and design decisions | Diagram tracked in JDR-32; website page planned |
| Development guide | Git workflow, documentation-first development, testing workflow, naming, and formatting | [Git](git-conventions.md), [development](software-development-conventions.md), [C++](cpp-conventions.md), and [Python](python-conventions.md) conventions |
| Simulation and testing | Gazebo/PX4 setup, test commands, scenarios, requirement traceability, and results | Practical guides planned |
| Deployment and operation | Image publishing, Pi/Jetson startup, updates, health checks, rollback, and evidence retrieval | Planned |
| Roadmap and project status | Major goals, dependencies, open decisions, and verified progress | [Software roadmap](software-roadmap.md) |

## Source documents

This overview was prepared from the following working documents, reviewed November 11, 2026. Their open decisions and provisional criteria will need reconciliation as the implementation develops.

- **PRD_SAR_DRONE.docx** describes user needs, product goals, scope, constraints, and proposed release criteria.
- **DESIGN_SPEC_SAR_DRONE.docx** describes system responsibilities, architecture, interfaces, and implementation details to develop.
- **TEST_PLAN_SAR_DRONE.docx** describes test configurations, scenarios, evidence, and staged validation.

## Adding and maintaining documentation

- Put project documentation in this folder using descriptive lowercase filenames with hyphens.
- Begin each document with its purpose and enough context for a new teammate.
- Link new documents from this README with a short description.
- Use relative Markdown links between repository files so they work across branches and checkouts.
- Keep each convention in its dedicated document and link to it from related guides.
- Distinguish agreed decisions, proposals, and open questions.
- Update documentation with the behavior or interface change it describes.
- Include prerequisites, commands, and expected results in setup or verification instructions.
- Cite external references and record relevant decisions so teammates can trace their context.
- Review documentation through the branch and PR process described in the Git conventions.

These Markdown files will supply the GitHub Pages documentation website. Website setup follows review of this outline.

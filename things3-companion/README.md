# Things3 Companion (Personal)

This repository contains a proof-of-concept Android companion app and supporting infrastructure for integrating with **Things3**, a proprietary task management application by Cultured Code.

**Crucial Legal Disclaimer:** This project interacts with Things3's internal database through unofficial means. Cultured Code warns that direct database access can corrupt data. There is no public API. This repository is provided for **personal, non‑commercial** experimentation only. Distributing or commercializing any derivative application may violate Cultured Code's EULA, Terms of Service, and various intellectual property rights. Consult legal counsel before considering public use.

## Repository Structure

- `android-app/` – Kotlin/Jetpack Compose Android application skeleton.
- `ec2-server/` – Scripts and instructions for running the read-only GraphQL API and webhook handler on an AWS EC2 instance.
- `apple-automation/` – Apple Shortcut and iPad automation instructions used to create tasks in Things3.
- `third-party-automation/` – Setup notes for bridging webhook services (Zapier/IFTTT).

Each directory includes a README with setup details.

## License

The custom code in this repository is released under the MIT License. The external `evelion-apps/things-api` project is GPLv3 and must be obtained separately.

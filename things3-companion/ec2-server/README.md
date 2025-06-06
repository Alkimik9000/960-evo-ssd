# EC2 Server Setup

This directory contains scripts and instructions to configure an AWS EC2 instance that hosts a read-only GraphQL API for Things3 and a webhook handler to trigger iPad automation.

## Overview

1. `evelion-apps-things-api/` – placeholder for the API code (clone from GitHub).
2. `setup-scripts/` – shell scripts to install dependencies and configure the API server.
3. `webhook-handler/` – simple Python server that receives webhook requests and triggers an Apple Shortcut via SSH.

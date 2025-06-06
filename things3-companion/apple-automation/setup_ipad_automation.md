# iPad Automation Setup

1. Enable **Things URLs** in Things3 settings and copy your auth token.
2. Import the `Things3_CreateTask_Shortcut.shortcut` into the Shortcuts app and edit it to include your auth token when constructing the URL scheme.
3. Ensure the Shortcut is named `CreateThingsTask` and accepts a JSON dictionary via the `Get Dictionary from Input` action.
4. Configure an SSH server or alternative trigger so the EC2 instance can remotely run this Shortcut.

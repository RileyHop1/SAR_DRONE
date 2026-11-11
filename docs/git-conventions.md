# Git Conventions

The team's branch, commit, and PR conventions from the November 10, 2026 Slack discussion. [Original Git Conventions document](https://jdr-khp4935.slack.com/docs/T0CEHC2VA7Q/F0CGNGGGHTL)

## Branch names

Use `JDR-ticketNumber-goal-of-branch`, such as `JDR-42-add-battery-monitoring`.

- Include the JDR ticket number.
- Describe the branch's goal in a few hyphenated words.

[Branch naming discussion](https://jdr-khp4935.slack.com/archives/C0CEK8YD6RY/p1794361824912689)

## Commit messages

Use `Type-what-you-did` with a short description of the actual change.

| Type | Purpose | Example |
| --- | --- | --- |
| Feat | New functionality | `Feat-add-flight-status-display` |
| Fix | Bug fixes | `Fix-correct-voltage-reading` |
| Doc | Documentation changes | `Doc-update-setup-guide` |

Additional types can be agreed as needed. [Commit naming discussion](https://jdr-khp4935.slack.com/archives/C0CEK8YD6RY/p1794361787246639)

## Pull request descriptions

Use these four headings in this order.

```markdown
# Changes
What changed?

# Goal
Why was this change needed?

# Steps to test
How can a teammate verify it?

# Pictures
Screenshots or images, if relevant. Otherwise N/A.
```

[PR description discussion](https://jdr-khp4935.slack.com/archives/C0CEK8YD6RY/p1794361919632029)

## Related workflow requirements

See [software development conventions](software-development-conventions.md) for the testing and merge requirements developed during software planning. This file records the naming and PR conventions from Slack.

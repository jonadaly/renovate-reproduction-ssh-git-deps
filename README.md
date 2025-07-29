Minimal reproduction for renovate git deps issue with SSH + tag.

## Current behavior

Renovate does not update the git dependencies in `pyproject.toml` that are specified via SSH and tag, and instead produces the following error:

```
ERROR: Request Error: cannot parse url (repository=jonadaly/renovate-reproduction-ssh-git-deps)
       "url": "/graphql",
       "baseUrl": "ssh://github.com/api/",
       "resolvedUrl": "ssh://github.com/api/graphql"
```

## Expected behavior

Renovate should update the git dependencies to the latest available version.

## Link to the Renovate issue or Discussion

https://github.com/renovatebot/renovate/discussions/37207

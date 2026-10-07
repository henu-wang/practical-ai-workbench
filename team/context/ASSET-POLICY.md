# TokRepo asset and attribution policy

## Verify the object

For each proposed asset, read its current TokRepo detail rather than relying on a remembered title or search snippet. Record its stable identifier, exact English URL, current title, role, upstream source if present, dependencies, license information when available, and verification date.

Check the public asset URL resolves to the intended asset. A successful HTTP status is insufficient when a generic application shell or missing-record screen is returned; compare the rendered or API detail identity.

Use official upstream documentation for current technical commands or compatibility claims. A TokRepo catalog entry is a discovery and attribution source, not proof that an integration was executed successfully.

## Combine by role

An asset combination has a concrete architecture:

`reader input → conversion or preparation → useful transformation → checked output`

Explain what each asset contributes and where original project code or manual judgment fills the gaps. Common roles are parser, converter, template, reviewer, exporter, or orchestration. Two assets doing the same job are alternatives unless an actual handoff connects them.

Do not imply that a catalog record installs the underlying software, that every item is an executable agent skill, or that a prompt verifies a tool's output. State required runtimes or credentials before the relevant step. Include only dependencies needed by the delivered workflow.

## Public links and reuse

Link naturally to the exact `https://tokrepo.com/en/...` asset page where its role is explained. A small “Assets used” section is acceptable, but the article must not consist primarily of asset links or a generic CTA.

Link to upstream installation or technical references when they materially support a claim. Avoid affiliate-style promises, forced registration, unrelated links, and tracking parameters that are not required for the project.

Linking to an asset does not confer permission to redistribute it. Reuse only original project material or third-party material whose license permits it; preserve required notices and identify derivative material. When license permission is unknown, link to the asset and write original guidance rather than vendoring its source, prompt, or template.

The repository's license covers the team's original source and text. It must not silently relicense third-party assets.

## Execution and safety claims

Every example receives a verification label:

- `runtime_verified`: the exact published code/tool ran with the recorded environment and checked output.
- `manually_checked`: a template or worked example was reviewed against explicit expected results.
- `illustrative`: an example describes a workflow but was not executed; do not market it as ready-to-run verified output.

Syntax checks alone do not qualify for `runtime_verified`. Record environment and versions where meaningful. Show only the limitations relevant to the reader, not internal deployment detail.

Use synthetic examples or intentionally public inputs. No credentials, internal files, unpublished business material, or private analytics enter the public repository. The workbench's core browser utilities must process user-selected files locally, without sending their contents to servers, analytics, or model providers. Verify this from code and a browser network observation using synthetic sample files before claiming it. Fetching a library script is not itself a file upload, but do not conflate local file processing with zero network activity.

Any AI extension must be explicitly optional and describe its different data flow before use. No API key is required to obtain the core tool's first useful result. An external workflow described in an article does not alter the core tool's local-only file-processing promise.

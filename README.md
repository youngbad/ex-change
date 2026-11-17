# ex-change

Currency exchange management system project.

The repository is currently at the discovery and foundation stage; it is not an
operational exchange system and makes no legal-compliance or production-readiness
claim.

- [As-is analysis](docs/AS_IS_ANALYSIS.md)
- [Target architecture](docs/TO_BE_ARCHITECTURE.md)
- [Regulatory requirements and review caveats](docs/REGULATORY_REQUIREMENTS.md)
- [Proposed database design](docs/DATABASE_DESIGN.md)
- [Security requirements](docs/SECURITY_REQUIREMENTS.md)
- [Implementation roadmap](docs/IMPLEMENTATION_ROADMAP.md)
- [Implementation status](docs/IMPLEMENTATION_STATUS.md)
- [Architecture decisions](docs/ADR/)

The initial `Money` domain primitive can be checked with:

```sh
python -m unittest discover -s tests -v
```

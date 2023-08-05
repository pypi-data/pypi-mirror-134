# Contributing To AutoTransform

AutoTransform is a tool built by and for developers and welcomes developers pushing their components and improvements upstream. While new components are the easiest things to push upstream new functionality and improvements to existing functionality are welcome as well.

#### What Should Push Upstream?

Upstream changes are intended to support the wider AutoTransform community. Bespoke components and changes unique to an organization should not be pushed upstream.

#### What Should I Know When Developing For AutoTransform?

- **Backwards compatability**: Recognize that AutoTransform is intended to be extended by organizations through development of bespoke components. If a change you are pushing upstream would break existing deployments of AutoTransform (i.e. by changing APIs) you are expected to provide a package that can be used to update existing deployments. Core developers MAY from time to time release breaking changes without providing a package for existing deployments but this will be heavily weighted against the cost of manual updates.
- **Test thoroughly**: The nature of AutoTransform means large automated changes without human review may be landed using this tool. All components and changes to AutoTransform must be tested thoroughly to ensure maximum safety given the potential damage. Unit tests should be included with all components.
- **Follow style and practice**: Because AutoTransform is expected to be extended often, it's important that we follow consistent style and practice to ease developers extending AutoTransform.
 - [**mypy**](https://pypi.org/project/mypy/) is used for type checking of AutoTransform and type hints should always be provided. 
 - [**black**](https://pypi.org/project/black/) is used for formatting AutoTransform with the following options:
   - --line-length=100
 - [**pylint**](https://pypi.org/project/pylint/) is used for linting with the following options:
   - --enable=W0611,R0201,R0902,R0903,R0913,R1732
   - --disable=R0801

#### I Want To Contribute, What Should I Do?

If after seing the above you still want to contribute to AutoTransform, follow standard Github practices by forking the repo, making changes, and submitting pull requests. If you are interested in becoming a frequent contributor with access to the repo reach out to nathro.software@gmail.com
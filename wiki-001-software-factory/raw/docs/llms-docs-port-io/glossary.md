---
title: "Glossary"
subtitle: "Understand AI software factories, the agentic SDLC, the context lake, and Port terms such as blueprint, entity, and scorecard."
authors: []
published_date: null
source_url: https://docs.port.io/glossary.md
origin: llms-txt
llms_txt: https://docs.port.io/llms.txt
section: "glossary"
fetched: 2026-10-25T18:18:27Z
---

# Glossary

Start here

* **[AI software factory](/glossary/.md#ai-software-factory)**: one place to build, govern and operate the Agentic SDLC.
* **[Agentic SDLC](/glossary/.md#agentic-sdlc)**: The software development lifecycle that your factory runs, with agents doing work and people directing and reviewing it.
* **[Context lake](/glossary/.md#context-lake)**: The shared engineering knowledge that gives your agents and teams organizational context.

Port uses several proprietary terms that either carry specific meaning within Port or collide with common industry concepts. This page defines each term precisely to eliminate ambiguity.

Terms are listed alphabetically.

***

### Access token[​](#access-token "Direct link to Access token")

Port's own bearer token, used to authenticate requests to the Port API. Generate one with the "Generate API token" button in your profile credentials, or via `POST /v1/auth/access_token`. An access token is valid for 3 hours, after which you need to generate a new one. Not to be confused with a third-party access token - such as a GitHub, GitLab, or Jira API token - supplied when configuring an [integration](#integration), or with the OAuth `response_type=token` implicit grant, which is an unrelated authorization flow.

[Learn more](/api-reference/create-an-access-token/)

***

### Agentic SDLC[​](#agentic-sdlc "Direct link to Agentic SDLC")

The software development lifecycle when AI agents carry out its stages - spec, plan, build, test - while people set the intent, review the work, and own the decision to deploy. The agentic SDLC is the process. A [software factory](#software-factory) is what you build in Port to run it.

[Learn more](/getting-started/agentic-sdlc-pillars/.md)

***

### AI agent[​](#ai-agent "Direct link to AI agent")

A Port-native AI agent that can query the [software catalog](#software-catalog), trigger [self-service actions](#self-service-action), and answer questions using Port as context. Distinct from generic AI agents - a Port AI agent has direct access to your catalog data model and organizational context.

[Learn more](/agent-management/custom-agents/overview/.md)

***

### AI software factory[​](#ai-software-factory "Direct link to AI software factory")

The system you build to run your [agentic SDLC](/glossary/.md#agentic-sdlc), coordinating AI agents, people, and tools from planning through deployment and operations. Shared context, workflows, governance, and measurement let agents carry out work while your engineers direct it and review the results. Port provides the platform for building and operating this system on top of your existing tools. In these docs, [software factory](/glossary/.md#software-factory) refers to the same concept.

Read the [AI software factory definition on port.io](https://www.port.io/glossary/ai-software-factory) and explore the [six platform pillars](/getting-started/agentic-sdlc-pillars/.md).

***

### Automation[​](#automation "Direct link to Automation")

An event-triggered workflow in Port that executes automatically when a catalog event occurs - for example, an entity was created, a property changed, or a timer expired. Distinct from a [self-service action](#self-service-action), which is triggered manually by a user.

[Learn more](/workflows/actions-and-automations/define-automations/.md)

***

### Blueprint[​](#blueprint "Direct link to Blueprint")

Port's schema definition for a catalog type. A blueprint defines the structure (properties, relations) that all instances of that type share - for example, "Microservice", "Environment", or "Team". Not to be confused with an architecture blueprint or system design document. In Port, a blueprint is closer to a class definition in object-oriented programming.

[Learn more](/context-lake/data-model/setup-blueprint/overview/.md)

***

### Catalog auto-discovery[​](#catalog-auto-discovery "Direct link to Catalog auto-discovery")

Port's ability to automatically detect and ingest resources from connected tools without requiring manual mapping configuration. When enabled, Port scans connected integrations and proposes or creates [entities](#entity) based on what it finds.

[Learn more](/context-lake/ingestion/catalog-auto-discovery/.md)

***

### Connector[​](#connector "Direct link to Connector")

Three unrelated concepts share this word, depending on context.

#### Context Lake connector[​](#context-lake-connector "Direct link to Context Lake connector")

The configuration object in Port that represents a connected [integration](#integration) and its sync settings, shown on the Connectors page (`Settings → Connectors`). Each installed integration creates a connector entry in your portal, which controls how data is fetched and [mapped](#mapping) into the catalog.

#### MCP connector[​](#mcp-connector "Direct link to MCP connector")

A routing configuration in Port that exposes an external MCP server's tools to developers and [AI agents](#ai-agent) through Port's governed MCP gateway.

#### SSO connector[​](#sso-connector "Direct link to SSO connector")

Such as the AD/LDAP connector, this is the bridge Auth0 uses to authenticate users against an external identity system like Active Directory.

Not to be confused with an [integration](#integration), which describes the underlying sync mechanism a Context Lake connector is built on.

[Learn more about MCP connectors](/agent-management/mcp-connectors/.md) - [learn more about the LDAP connector](/platform-administration/sso-authentication/sso-providers/ldap/.md)

***

### Context Lake[​](#context-lake "Direct link to Context Lake")

Port's aggregation layer that collects catalog data, events, and metadata to provide AI agents and tools with rich organizational context. The Context Lake is what makes Port-connected AI agents aware of your specific infrastructure, services, and relationships.

[Learn more](/context-lake/overview/.md)

***

### Entity[​](#entity "Direct link to Entity")

A catalog record - a concrete instance of a [blueprint](#blueprint). If "Microservice" is a blueprint, then "payment-service" is an entity of that blueprint. Entities hold the actual data (property values, relation links) for each resource tracked in Port. Not to be confused with a generic ORM entity or domain entity in domain-driven design.

[Learn more](/context-lake/ingestion/ingest-data-into-port/native-integrations/overview/.md)

***

### Environment[​](#environment "Direct link to Environment")

An ambiguous term with three meanings depending on context. It can be a property value or dedicated blueprint/[entity](#entity) type used to distinguish deployment stages (e.g., Production, Staging). It can also be a generic OS or CI/CD environment variable, unrelated to Port's data model. Finally, "your second Port environment" refers to an entirely separate Port organization/[portal](#portal) instance - for example, when migrating configuration between a staging and production Port account. Check the surrounding context to determine which meaning applies.

[Learn more](/guides/all/move-port-configurations-between-environments-with-port-ai-and-github-mcp/.md)

***

### Execution agent[​](#execution-agent "Direct link to Execution agent")

A self-hosted relay binary (`port-agent`) that lets [self-service actions](#self-service-action) and [workflow](#workflow) webhook nodes reach services inside a private network, without exposing a public endpoint. It has no AI capabilities and is unrelated to the [AI agent](#ai-agent) feature - despite the shared word "agent," the execution agent only relays webhook calls over Kafka.

[Learn more](/workflows/build-workflows/nodes/action-nodes/port-execution-agent/.md)

***

### Integration[​](#integration "Direct link to Integration")

In Port, an integration is an [Ocean](#ocean)-based connector that syncs data from a third-party tool (GitHub, Jira, AWS, Datadog, and others) into the [software catalog](#software-catalog). The term is specific to Port's integration layer and is not a generic synonym for any API connection.

[Learn more](/context-lake/ingestion/ingest-data-into-port/native-integrations/overview/.md#available-plug--play-integrations)

***

### Kind[​](#kind "Direct link to Kind")

The API object type that a [mapping](#mapping) [resource](#resource) fetches from an integration - for example `repository`, `pull-request`, or `issue`. Defined as the `kind` field inside a `resources` block. Not to be confused with a Kubernetes manifest's own `kind` field (e.g., `kind: Deployment`), which frequently appears in the same guide when Port ingests Kubernetes resources.

[Learn more](/context-lake/ingestion/configure-mapping/overview/.md#resources-and-kinds)

***

### Level[​](#level "Direct link to Level")

A tier within a [scorecard](#scorecard) (e.g., Basic, Bronze, Silver, Gold). An entity reaches a level when all [rules](#rule) defined for that level pass. Levels are ordered - an entity must satisfy lower levels before achieving higher ones.

[Learn more](/governance/standards-and-compliance/overview/.md)

***

### Mapping[​](#mapping "Direct link to Mapping")

The JQ-based configuration within a [connector](#context-lake-connector) that translates external tool data into Port [entities](#entity). Mapping defines which data maps to which [blueprint](#blueprint) and what value each [property](#property) receives.

[Learn more](/context-lake/ingestion/configure-mapping/overview/.md)

***

### MCP server[​](#mcp-server "Direct link to MCP server")

Port's implementation of the Model Context Protocol (MCP), which exposes catalog data and [self-service actions](#self-service-action) to external AI tools such as Claude, Cursor, and GitHub Copilot. Connecting an AI tool to Port's MCP server gives it live access to your catalog and the ability to trigger actions on your behalf.

[Learn more](/agent-management/port-mcp-server/overview/.md)

***

### Meta-property[​](#meta-property "Direct link to Meta-property")

A reserved property such as `$identifier`, `$title`, `$team`, or `$createdAt` that exists on every [entity](#entity) by default, always prefixed with `$`. Meta-properties look like ordinary [properties](#property) in mapping and rule syntax but are managed by Port rather than defined on the [blueprint](#blueprint).

[Learn more](/context-lake/data-model/setup-blueprint/properties/meta-properties/.md)

***

### Ocean[​](#ocean "Direct link to Ocean")

Port's open-source integration framework used to build and run integrations that sync data from external tools into the [software catalog](#software-catalog). Ocean is Port-specific - it is not a general industry term. When Port documentation refers to "Ocean integrations", it means integrations built on this framework.

[Learn more](https://www.github.com/port-labs/ocean)

***

### Ownership[​](#ownership "Direct link to Ownership")

The mechanism in Port for assigning a [team](#team) as the responsible owner of an [entity](#entity). Ownership is used to drive accountability, filter catalog views, and scope [RBAC](#rbac) permissions - for example, restricting who can trigger actions on a given service.

[Learn more](/context-lake/business-context/ownership/.md)

***

### Page[​](#page "Direct link to Page")

A customizable view within Port's [portal](#portal). Pages can display catalog tables, dashboards, entity detail views, or embedded content. In Port, "page" refers specifically to a portal view, not a generic web page.

***

### Plugin[​](#plugin "Direct link to Plugin")

Port's first-class object for a custom-built web UI - developed locally as a single HTML file and uploaded through the Port plugins CLI or [Port MCP server](#mcp-server) - that powers custom widgets on dashboards and entity pages. Not to be confused with a third-party tool plugin referenced in integration guides, such as a Jenkins plugin or Backstage's TechDocs plugin, which has no relation to Port's plugin API.

[Learn more](/interface-builder/port-interface/plugins/.md)

***

### Portal[​](#portal "Direct link to Portal")

Port's web app, the interface to your software factory. At [app.port.io](https://app.port.io), you interact with the catalog, run [self-service actions](/glossary/.md#self-service-action), and view [scorecards](/glossary/.md#scorecard). "Your portal" refers to your organization's Port instance.

[Docs home](/index.md)

***

### Property[​](#property "Direct link to Property")

A field defined on a [blueprint](#blueprint) that holds data for each [entity](#entity) (e.g., `language`, `repo_url`, `on_call_contact`). Port supports many property types including strings, numbers, booleans, URLs, and various computed types.

[Learn more](/context-lake/data-model/setup-blueprint/properties/overview/.md)

***

### Provider[​](#provider "Direct link to Provider")

An umbrella term with several unrelated meanings depending on the page. A Git provider (GitHub, GitLab, Bitbucket) is the source Port ingests repository and pull request data from. An LLM provider (OpenAI, Anthropic, AWS Bedrock) is the model backend configured for Port AI. A login/identity provider (Auth0) handles SSO authentication. The Terraform `provider "port" {}` block configures the Port Terraform provider itself. Check the surrounding context to determine which provider a page is referring to.

[Learn more about LLM providers](/port-ai/llm-providers-management/overview/.md)

***

### RBAC[​](#rbac "Direct link to RBAC")

Role-based access control as implemented in Port. Port's RBAC model controls which users can view, create, edit, or delete entities and blueprints, and who can trigger [self-service actions](#self-service-action). Default roles include Admin and Member; teams can also be used to scope permissions.

[Learn more](/context-lake/consuming-the-lake/govern-data-access/overview/.md)

***

### Relation[​](#relation "Direct link to Relation")

A typed link between two [blueprints](#blueprint) that models dependencies or ownership in the catalog (e.g., a Microservice belongs to a Team, a Deployment references an Environment). Relations in Port are directional and defined at the blueprint level - not to be confused with a relational database foreign key.

[Learn more](/context-lake/data-model/setup-blueprint/relate-blueprints/.md)

***

### Resource[​](#resource "Direct link to Resource")

Within a [mapping](#mapping) configuration, a resource is a single block that specifies a [kind](#kind) to fetch and how to map it to a [blueprint](#blueprint). Elsewhere in the docs, "resource" is also used generically to describe any infrastructure or cloud object (a Kubernetes cluster, an S3 bucket) tracked in the [software catalog](#software-catalog) - this generic usage does not refer to the `resources` mapping key specifically.

[Learn more](/context-lake/ingestion/configure-mapping/overview/.md#resources-and-kinds)

***

### Rule[​](#rule "Direct link to Rule")

A single condition within a [scorecard](#scorecard) level (e.g., "has\_owner = true", "response\_time < 200"). Rules evaluate [entity](#entity) property values and return pass or fail for each entity.

[Learn more](/governance/standards-and-compliance/overview/.md)

***

### Run[​](#run "Direct link to Run")

A single execution of a [workflow](#workflow) or [self-service action](#self-service-action), including its inputs, status, logs, and audit trail. Runs are stored in Port and can be inspected after the fact to understand what was triggered, by whom, and what the outcome was.

[Learn more](/workflows/actions-and-automations/reflect-action-progress/.md)

***

### Scorecard[​](#scorecard "Direct link to Scorecard")

Port's mechanism for tracking compliance, quality, and maturity standards across catalog [entities](#entity). A scorecard defines a set of [levels](#level) and [rules](#rule) and evaluates each entity against them. Not a generic KPI dashboard - scorecards in Port are integrated directly with the catalog data model and update in real time as entity data changes.

[Learn more](/governance/standards-and-compliance/overview/.md)

***

### Secret[​](#secret "Direct link to Secret")

Three distinct concepts share this word. A Port secret is an encrypted value stored in your organization's Secrets tab (under Credentials) and referenced by identifier in [integrations](#integration) and [self-service actions](#self-service-action). A Secret input is a self-service action input type that encrypts its value before sending it to your backend. A CI/CD secret - for example `${{ secrets.PORT_CLIENT_SECRET }}` in a GitHub Actions workflow - is stored in your Git [provider](#provider), unrelated to Port's own Secrets tab.

[Learn more](/platform-administration/secrets-management/port-secrets/.md)

***

### Self-service action[​](#self-service-action "Direct link to Self-service action")

A user-triggered workflow in Port that lets developers perform predefined operations (provision resources, open tickets, deploy services) directly from the portal. Distinct from [automations](#automation), which are triggered automatically by catalog events rather than by a user. Often shortened to "action" in Port documentation.

[Learn more](/workflows/actions-and-automations/create-self-service-experiences/.md)

***

### Skill[​](#skill "Direct link to Skill")

A reusable AI capability registered in Port that [AI agents](#ai-agent) can invoke to perform specific tasks (e.g., deploy a service, open a pull request, query the catalog). Skills are defined once and can be called by any agent that has access to them.

[Learn more](/agent-management/skills/overview/.md)

***

### Software catalog[​](#software-catalog "Direct link to Software catalog")

The central registry in Port that contains all [entities](#entity), organized by [blueprints](#blueprint) and linked by [relations](#relation). The software catalog is the core of Port, giving teams a unified, queryable view of their infrastructure, services, and resources.

[Learn more](/context-lake/overview/.md)

***

### Software factory[​](#software-factory "Direct link to Software factory")

In these docs, shorthand for [AI software factory](/glossary/.md#ai-software-factory): the system you build on Port to run your [agentic SDLC](/glossary/.md#agentic-sdlc) at scale. This differs from the older industry use of software factory to mean an outsourced development shop.

[Learn more](/index.md)

***

### Team[​](#team "Direct link to Team")

A group of users in Port, used for ownership assignment and RBAC. Teams in Port are also first-class [entities](#entity) in the catalog (a built-in blueprint), meaning they can hold [properties](#property), participate in [relations](#relation), and appear in catalog views.

[Learn more](/platform-administration/users-and-teams/manage-users-teams/.md)

***

### Workflow[​](#workflow "Direct link to Workflow")

Port's orchestration feature for sequencing multiple steps - actions, conditions, loops - into a multi-step automated process. Not to be confused with CI/CD "workflows" such as GitHub Actions workflows - a Port Workflow is a higher-level orchestration construct within Port itself.

[Learn more](/workflows/overview/.md)

## FAQ[​](#faq "Direct link to FAQ")

1What is the difference between a blueprint and an entity?

2How is an AI agent different from the execution agent?

3What is the difference between an automation and a self-service action?

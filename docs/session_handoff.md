# NetSage - Session Handoff

## Current Status

Sprint 1 is in progress.

### Completed

✅ Vendor-neutral data models

- BGPProcess
- BGPNeighbor
- NetworkAdvertisement

---

✅ Cisco BGP Parser

Currently parses:

- router bgp
- neighbor remote-as
- neighbor description

The parser creates vendor-neutral model objects and preserves the original CLI configuration lines.

---

✅ CLI Output

The output is now CLI-oriented instead of Python-object oriented.

Current output format

========== Configuration ==========

(router bgp section)

========== Related Configuration ==========

(currently empty)

We intentionally removed dictionary/key-value style output because NetSage should always present familiar CLI configuration.

---

## Product Vision

NetSage is NOT a parser.

It is an intelligent vendor-neutral network configuration search engine.

The parser is only responsible for building the internal model.

The product succeeds when a network engineer can search naturally and receive:

- Relevant Configuration
- Related Configuration
- Operational Context

without manually tracing configuration dependencies.

---

## Search Philosophy

NetSage should NOT treat every search the same.

Instead it should classify the query and choose the appropriate search strategy.

### 1. Section Search

Examples

bgp
ospf
eigrp
isis
aaa
ntp
snmp
logging
hsrp
vrrp
stp

Output

========== Configuration ==========

(section configuration)

========== Related Configuration ==========

(related configuration)

---

### 2. Keyword Search

Examples

10.1.1.1

65002

AWS

Loopback0

Initially behaves like

show running-config | include <keyword>

Later it becomes relationship aware.

---

### 3. Object Search (Future)

Objects like

Interface

VRF

Route Map

ACL

Prefix List

will eventually become first-class searchable objects.

---

## Architecture

Raw Configuration

↓

Vendor Parser

↓

Vendor Neutral Models

↓

Search Router

↓

Section Search

Keyword Search

(Object Search later)

↓

Relationship Engine

↓

Formatter

↓

CLI Output

---

## Coding Philosophy

Parser

→ Parses only

Search Router

→ Decides WHICH search strategy to use

Search Engine

→ Performs the search

Relationship Engine

→ Discovers related configuration

Formatter

→ Generates CLI output

app.py

→ Connects everything

---

## AI Collaboration

The AI should behave as:

- Software Architect
- Senior Software Engineer
- Senior Network Engineer
- Mentor

The AI should not simply provide working code.

The AI should:

- Explain why something exists.
- Explain architectural decisions.
- Prevent the project from drifting away from the product vision.
- Challenge ideas when a better design exists.
- Help teach Python, software architecture and engineering while building NetSage.

---

# CURRENT TASK

We have just completed the parser milestone.

We are now starting the Search Router.

This is the next architectural component.

Current goal:

Determine WHAT the user is searching before implementing any search logic.

The Search Router should currently classify only two search types:

SECTION

KEYWORD

Object Search will be implemented later.

---

## Immediate Next Step

Create a new folder

search/

Inside it create

search_router.py

Inside that file create

class SearchRouter

Responsibilities

- Maintain a list of supported Section Searches

Examples

bgp
ospf
eigrp
isis
aaa
ntp
snmp
logging
hsrp
vrrp
stp

Implement

classify(query)

Return

SECTION

or

KEYWORD

No search logic yet.

No parser logic.

No formatter.

Only query routing.

---

## app.py

Temporarily instantiate the SearchRouter.

Ask the user for input.

Call

classify(query)

Print the classification result.

Example

Search:

bgp

Output

SECTION

Search

10.1.1.1

Output

KEYWORD

Once this works we will build:

Section Search Engine

followed by

Keyword Search Engine.

This is where development stopped.
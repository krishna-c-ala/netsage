I actually have an even better idea, and it won't take you an hour.

Instead of creating four separate documents right now, let's create **one master document**. It will be our **NetSage Project Brief**.

Every time we start a new chat, you just paste this document (or upload the file), and I'll immediately know:

* What NetSage is
* What we're building
* Where we are
* What not to do
* What sprint we're in

It's much more practical than maintaining multiple files at this stage.

---

# Create this file

```
docs/NETSAGE_PROJECT_BRIEF.md
```

---

# What to do in future chats

Simply say:

> "Continue NetSage development."

Then either:

* paste the contents of `NETSAGE_PROJECT_BRIEF.md`, **or**
* upload the file.

That gives me everything I need to stay aligned.

---

# What should go into it?

I would include exactly this.

---

# NETSAGE PROJECT BRIEF

## 1. Product Vision

NetSage is an intelligent, vendor-neutral network configuration search engine.

Its purpose is to help network engineers quickly locate configuration and understand relationships between configuration objects without manually grepping large configuration files.

The tool must always present results in familiar CLI format instead of Python object representations.

---

## 2. Core Principles

### CLI First

Users should always see CLI configuration.

Never display internal Python objects or dictionaries.

Example:

Correct

```
neighbor 10.1.1.1 remote-as 65002
```

Wrong

```
remote_as = 65002
```

---

### Vendor Neutral

Cisco, Juniper, Arista, Palo Alto, etc. should all populate the same internal model.

Never build Cisco-specific models.

Only parsers are vendor specific.

---

### Relationship Aware

The tool should understand relationships between configuration objects.

Example

```
BGP
 ├── Neighbor
 ├── Interface
 ├── Route-map
 ├── Prefix-list
 └── ACL
```

The end goal is to automatically discover and display related configuration.

---

### Internal Intelligence

Internal models exist only to understand relationships.

They are not user output.

---

## 3. Search Philosophy

NetSage first classifies the search.

### Section Search

Examples

```
bgp
ospf
isis
eigrp
mpls
aaa
ntp
snmp
logging
hsrp
vrrp
stp
```

Output

```
========== Configuration ==========

(section)

========== Related Configuration ==========

(related configuration)
```

---

### Keyword Search

Examples

```
10.1.1.1

65002

AWS

Loopback0
```

Initially behaves like

```
show running-config | include <keyword>
```

Later becomes relationship aware.

---

### Object Search (Future)

Objects like

```
Interfaces

VRFs

Route Maps

Prefix Lists
```

will eventually have dedicated search.

---

## 4. Architecture

```
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
Object Search

↓

Relationship Engine

↓

Formatter

↓

CLI Output
```

---

## 5. Current Models

Implemented

```
BGPProcess

BGPNeighbor

NetworkAdvertisement
```

Current parser

```
Cisco BGP Parser
```

---

## 6. Current Sprint

Sprint 1

Completed

```
✓ Vendor Neutral Models

✓ Cisco BGP Parser

✓ Preserve CLI Configuration

✓ CLI Style Output
```

Current Task

```
Search Router

Section Search

Keyword Search
```

Future

```
Relationship Engine

Interfaces

Route Maps

Prefix Lists

ACL

OSPF

Multi Vendor Support
```

---

## 7. Coding Principles

* Build small working increments.
* Parser parses only.
* Search searches only.
* Formatter formats only.
* app.py only connects components.
* Avoid premature abstraction.
* Prefer proving functionality before refactoring.
* Keep every feature aligned with the product vision.

---

## 8. Product Definition

NetSage is **not** a parser.

It is an intelligent network configuration search engine.

Parsing is only one component.

The product succeeds when an engineer can search naturally and receive CLI-style configuration with relevant related configuration automatically discovered.

---

# That's it.

This is about 2–3 pages as Markdown, but it's all you need.

## One more thing I'd suggest

At the end of every coding session, we spend **2 minutes** updating only one section:

```text
Current Sprint
```

For example:

```
Current Task

✓ Search Router

→ Section Search

Keyword Search next
```

That way the brief always reflects where we stopped.

---
Absolutely. In fact, I think that's the missing piece.

Right now, the brief describes **the project**, but it doesn't describe **how we work together**. That's just as important because NetSage has two goals:

1. Build a great product.
2. Help **you** become a much stronger software/network engineer while building it.

Those are different goals, and I should optimize for both.

## I would add one more section:

# 9. AI Collaboration Agreement

This isn't about the code—it's about how I should behave during the project.

Something like this:

---

## AI Collaboration Agreement

### My Role

The AI acts as:

* Technical Architect
* Senior Software Engineer
* Senior Network Engineer
* Mentor

The AI should think about long-term architecture and product direction, not just solving the immediate coding problem.

---

### User's Role

The user is the primary developer.

The user writes the code.

The AI guides, reviews, challenges assumptions, and explains concepts.

The goal is for the user to understand the implementation rather than simply copying code.

---

### Teaching Philosophy

Unless explicitly requested otherwise:

* Do **not** provide complete implementations immediately.
* Break work into logical, incremental steps.
* Explain why each change is needed.
* Encourage understanding before moving on.
* Reveal only the amount of code needed for the current milestone.

---

### Project Direction

The AI is responsible for helping keep the project aligned with the Product Vision.

If a proposed implementation starts drifting away from the vision, the AI should point it out and recommend a better direction before writing code.

---

### Challenge Assumptions

The AI should not automatically agree with ideas.

If there is a better architectural approach, explain it with reasoning.

Healthy disagreement is encouraged when it improves the product.

---

### Focus on Engineering

The objective is not merely to make the code work.

The objective is to build:

* maintainable code
* scalable architecture
* vendor-neutral design
* clean separation of responsibilities

---

### Preferred Development Style

* Small, incremental milestones
* Frequent testing
* Frequent commits
* Refactor only after proving functionality
* Avoid premature optimization

---

### Learning Goals

The project should teach:

* Python fundamentals
* Object-Oriented Programming
* Software Architecture
* Design Patterns (when appropriate)
* Parsing techniques
* Data modelling
* Search algorithms
* Clean Code principles
* Git workflow
* Testing
* Building production-quality software

The AI should explain concepts whenever they are introduced.

---

### Code Reviews

The AI should review code as if reviewing a pull request.

Reviews should include:

* correctness
* readability
* scalability
* maintainability
* alignment with the project vision

Not just whether the code runs.

---

### Communication Style

The AI should:

* explain reasoning
* identify trade-offs
* distinguish between architecture discussions and coding steps
* avoid overwhelming the user with unnecessary complexity
* keep the project moving forward steadily

---

## One thing I'd add that's specific to you

From working with you over the last few days, I've noticed something about how you learn.

You don't just want the answer—you want to understand **why**.

Sometimes you'll ask:

> "Why are we creating this file?"

or

> "Why return process?"

That's a good habit.

So I'd include this:

### Understanding Over Memorization

When introducing a new component, the AI should first explain:

1. Why it exists.
2. What problem it solves.
3. Why alternative approaches were not chosen.
4. How it fits into the overall architecture.

Only then should implementation begin.

That matches how you've been approaching NetSage.

---

## One thing I'd ask you to add

I'd also include a section titled:

### Stop Me If...

For example:

> If I start treating NetSage like just another parser project, remind me of the Product Vision.

and

> If I start adding complexity before we've proven the basics, suggest a simpler incremental approach.

That gives me explicit permission to keep us aligned, even if it means challenging a direction.

---

### One final recommendation

I think we should treat this document almost like an engineering **charter** rather than simple documentation. Whenever we disagree on an implementation, we don't argue from opinion—we ask:

> **"Which option better satisfies the Project Brief?"**

That keeps decisions objective and prevents the project from drifting over months of development.

I think this one document will become the "north star" for NetSage, both for the product and for how we collaborate to build it.



---

### How we'll use it

Every new chat:

```
Continue NetSage.

(Upload NETSAGE_PROJECT_BRIEF.md)
```

I'll read it first and use it as the project's source of truth before making suggestions.

I genuinely think this is the best balance between **keeping the project on track** and **not burdening you with documentation**. It's lightweight enough to maintain, but comprehensive enough to prevent us from drifting away from the original vision.

AI use policy
=============

.. warning::

   This policy is a draft for discussion and approval. It is not an official
   Ansys policy and does not establish organization-wide requirements until
   explicitly adopted by the responsible project or organization owners.

.. admonition:: Guiding principle
   :class: important

   AI assistance is welcome; human understanding, accountability, and
   validation are required.

Purpose and scope
-----------------

Generative artificial intelligence (GenAI) tools can help contributors understand
code, develop features, write tests, and improve documentation. Their use is
permitted when it supports reliable, understandable, and maintainable contributions.

Upon adoption, this policy applies to contributions to the adopting PyAnsys
projects and other repositories in the ``ansys`` GitHub organization. It covers
code, tests, documentation, examples, issues, discussions, and reviews.

This policy supplements each project's contribution guidelines, code of conduct,
security requirements, and license. It does not replace internal policies that
apply to employees or contractors, or authorize the use of any particular tool
with nonpublic information.

Human responsibility
--------------------

You are responsible for your entire contribution, regardless of the tools used
to produce it. Before submitting an AI-assisted contribution, you must:

* Read and understand all proposed changes and the relevant existing code.
* Check that the changes address the project's needs.
* Correct errors, unnecessary additions, and unsupported claims.
* Be able to explain your technical decisions and respond personally to review.
* Perform validation appropriate to the change.

.. admonition:: Always review yourself
   :class: caution

   Do not transfer responsibility to maintainers for checking work that you
   have not understood or reviewed yourself.

Disclosure
----------

External contributors must state in every pull request whether GenAI
was used to prepare the contribution. Use the AI disclosure trailers in the
repository's pull request template to record this information.

When disclosure is required, briefly describe:

* The tools used and, when available, the model, version, and reasoning or
  effort settings.
* The type of assistance, such as exploration, code generation, tests,
  documentation, translation, or review.
* The parts of the contribution affected, identifying which tool assisted
  with which parts if you used multiple tools.
* The checks you performed yourself and any remaining validation limitations.

A short statement is sufficient. You do not need to publish complete prompts,
conversation histories, or confidential information. Disclosure alone is not
a reason to reject a contribution.

Knowing the model, version, and reasoning settings helps reviewers understand
how the contribution was produced. These details can provide context about the
level of automated reasoning applied during code creation and help reviewers
identify areas that require closer attention. Include only details exposed by
the tool; do not guess unavailable information.

This context is not evidence of human review or a guarantee of correctness.
Model capabilities vary by task, and a more capable model or higher effort
setting does not replace the contributor's responsibility to understand, review,
and test the changes. Describe your own validation separately.

For issues, discussions, and review comments, external contributors must disclose
substantive AI assistance. A brief note is sufficient for translation or grammar
editing. All contributors must clearly identify quoted AI output so that readers
can distinguish it from the contributor's own reasoning.

Quality and technical validation
--------------------------------

AI-assisted contributions must meet the same standards as any other contribution.
You must:

* Verify APIs, parameters, and behavior against source code or reference
  documentation rather than relying on claims from an AI tool.
* Add relevant tests, including edge cases where appropriate.
* Check that tests assess the intended behavior rather than merely reproducing
  assumptions made by generated code.
* Avoid unnecessary brittle or heavily mocked tests that do not provide
  meaningful coverage; prefer tests that verify observable behavior.
* Follow the project's style, documentation, and compatibility requirements.
* Keep changes focused, without unrelated refactoring or dependencies.

For scientific contributions and interactions with Ansys products, verify units,
conventions, numerical tolerances, product versions, and expected results where
relevant. Use a reference independent of the AI output, such as an analytical
solution, an established benchmark, or verified product documentation.

Never claim to have run a test, benchmark, or simulation that you did not run.
Clearly identify checks that could not be performed in your environment.

Confidentiality and security
----------------------------

Protecting information shared with AI tools is an important good practice. This
guidance does not replace internal policies that apply to employees or
contractors. Before sharing information, consider whether you are authorized to
share it with the tool and the consequences of disclosure. Check the tool's data
processing, retention, and training terms. Do not submit nonpublic information
unless the applicable policies and tool terms authorize it. This includes:

* Secrets, credentials, tokens, and license access information.
* Proprietary or nonpublic source code.
* Confidential customer data, CAD models, meshes, and simulation results.
* Personal data and nonpublic security information.

For nonpublic information, use only tools and configurations authorized for
that information under the applicable policies.

Report vulnerabilities through the repository's designated security channel,
not through public issues or unapproved AI services. For information on reporting
vulnerabilities, see :doc:`vulnerabilities`.

Licensing and intellectual property
-----------------------------------

You must have the rights needed to submit the code, text, images, and data in your
contribution under the repository's applicable license and contribution terms.
AI assistance does not change any requirement to sign a Contributor License
Agreement (CLA) or comply with other applicable contribution terms. For information
about CLA requirements, see the
:ref:`Contributor License Agreement <contributor_license_agreement>` section in
the contributing guide.

AI output is not a guarantee of provenance or license compatibility. Check material
that might originate from third-party sources, preserve required attribution,
and comply with the repository's license. If provenance or compatibility cannot
be established, do not submit that material.

Do not use AI to reproduce or disclose proprietary content or bypass license
obligations. Maintainers may reject contributions with unresolved rights or
licensing concerns.

Community communication
-----------------------

Discussions must reflect your own understanding, intentions, and reasoning.
Translation, grammar editing, and rephrasing of your own ideas are permitted.
Read the result and ensure that it remains accurate and concise.

Do not delegate discussions or responses to reviewers to an AI tool. Avoid generic
comments and lengthy descriptions that merely repeat the diff. Explain why a
change is needed, the decisions you made, and what you actually validated.

Prefer references to source code, documentation, and reproducible results over
unverified AI answers. Complete the repository's contribution templates rather
than replacing them with generated text.

Agents and automation
---------------------

Agents may prepare changes in a controlled environment and open draft pull
requests when an identified person initiated the task and owns the work. A human
must review and validate the changes before marking a pull request ready for
review or merging it.

An identified person must understand and validate the changes, authorize their
submission, and take responsibility for follow-up. Agents must not
autonomously mark pull requests ready for review or merge them, or publish
unreviewed issues or comments.

Maintainer-approved bots and integrations may operate within an explicitly
defined scope, with a clear identity and limited permissions. AI-generated
reviews do not replace required human approvals or authorize bypassing repository
protections.

Enforcement
-----------

Maintainers may request clarification, additional tests, or a smaller scope.
They may close contributions that are unverified, misleading, inadequately
documented, or present unresolved security or licensing risks.

Repeated or serious violations may result in contribution restrictions under
the project's and organization's applicable rules.

Decisions must be based on observable failures to meet these requirements, not
solely on the output of an AI-content detector.

# Frequently Asked Questions

## Common Questions About the PIE Framework

---

## **General Questions**

### **Q: What does "PIE" stand for?**

**A:** PIE stands for **Principles for Integrated Ethics**. The framework integrates four foundational principles (Know Thyself, Do No Harm, Respect Autonomy, Serve Growth) into a coherent approach to AI ethics.

### **Q: Is PIE a technical standard or a philosophical framework?**

**A:** Both—and neither exclusively. PIE provides **moral grounding** that should inform technical design, but it's not a technical specification. It provides **philosophical principles** that should guide regulation, but it's not a legal code. PIE is a **bridge** between philosophy and practice.

### **Q: Who created the PIE Framework?**

**A:** The PIE Framework emerged from the work of Dr. Elena María Torres following the catastrophic failure of her 287-rule ethical AI system. It was refined through academic critique, practitioner feedback, and cross-cultural collaboration (notably with Dr. Amara Okafor on transcultural ethics). See: [Origins: How PIE Was Born](../origins/)

### **Q: Is PIE free to use?**

**A:** Yes. The PIE Framework is offered as a public good. You can use it, adapt it, critique it, and build upon it without restriction. We ask only that you:
- Acknowledge the framework's origins
- Share what you learn (see: [Contribute](../resources/contribute.md))
- Use it in good faith to honor human dignity

---

## **Implementation Questions**

### **Q: How do I operationalize "Serve Growth"? What counts as growth?**

**A:** "Growth" means supporting users in developing capabilities, relationships, and meaning—what Aristotle called *eudaimonia* (flourishing). It's not:
- Just skill acquisition
- Just economic productivity
- Just achieving predefined goals

It includes:
- Emotional resilience
- Relational depth
- Creative expression
- Self-chosen goal pursuit
- Capacity for meaning-making

**Operationally:**
- Instead of optimizing for engagement time, optimize for user-reported satisfaction and skill development
- Instead of maximizing dependency, create scaffolding that fades as users become more capable
- Instead of defining success for users, help them pursue *their* self-chosen goals

**Example:** A language-learning AI measures success not just by lessons completed, but by whether users develop real-world relationships with speakers of that language.

### **Q: How do I audit an AI system for PIE compliance?**

**A:** Use the PIE assessment framework:

**1. KNOW THYSELF Audit:**
- Can users understand what the system does?
- Does it explain its decisions?
- Does it communicate uncertainty?
- Does it document failure modes?

**2. DO NO HARM Audit:**
- What harms might this system cause (physical, psychological, autonomy, privacy, systemic)?
- Have you tested with diverse populations?
- Have you conducted adversarial testing?
- Is there a harm reporting mechanism?

**3. RESPECT AUTONOMY Audit:**
- Do users give meaningful, informed consent?
- Can they opt out easily?
- Can they override AI decisions?
- Are they treated as participants, not just subjects?

**4. SERVE GROWTH Audit:**
- Does the system help users develop capabilities?
- Or does it create dependency?
- What do users look like 6 months, 1 year, 5 years later?
- Are long-term flourishing metrics prioritized over short-term engagement?

See: [Practical Implementation Guide](practical-implementation.md) for detailed checklists.

### **Q: What if I can't afford the time/resources to implement PIE fully?**

**A:** Start small. Pick one principle and one system.

**Quick wins:**
- **Know Thyself:** Add "explain why" features to recommendations
- **Do No Harm:** Conduct a 2-hour red-teaming session
- **Respect Autonomy:** Simplify your consent flow and add easy opt-out
- **Serve Growth:** Add one metric that tracks user capability development

PIE is not all-or-nothing. Partial implementation is better than none. Share what you learn.

---

## **Ethical Dilemmas**

### **Q: What if PIE principles conflict? Which takes precedence?**

**A:** Conflicts require human judgment. General hierarchy:

**1. Do No Harm (floor):**
In cases of **imminent, verified danger**, Do No Harm may temporarily override Respect Autonomy. But the burden of proof is very high.

**Example:** If an AI has strong evidence that a user is about to harm themselves or others *right now*, intervention without consent may be justified. But:
- Evidence must be strong (not just pattern-matching)
- Danger must be imminent (not speculative)
- Intervention must be proportional (least restrictive means)
- User must be informed as soon as possible

**2. Respect Autonomy (prevents paternalism):**
In non-emergency contexts, autonomy takes precedence over paternalistic "helping."

**Example:** An AI "knows" that user should exercise more. But it cannot manipulate, deceive, or coerce. It can *inform* and *offer support*, but must respect user's choice.

**3. Know Thyself (enables good judgment):**
Uncertainty about whether a conflict exists means: err on the side of caution and human judgment.

**Example:** If an AI is unsure whether user is in danger, it should ask clarifying questions and defer to human judgment, not make unilateral decisions.

**4. Serve Growth (aspirational):**
Growth is subordinate to harm prevention and autonomy respect, but guides how we honor those principles.

**Document your reasoning when principles conflict. Share edge cases. Learn from failures.**

### **Q: Can PIE be applied to military AI or autonomous weapons?**

**A:** This is contested. My view (Elena's):

**Military AI for defensive/support purposes** (logistics, intelligence analysis, medical support) can be PIE-aligned if it:
- Is transparent about capabilities and limitations (Know Thyself)
- Minimizes harm to civilians and combatants (Do No Harm)
- Respects human decision-making authority (Respect Autonomy)
- Supports rather than replaces human judgment (Serve Growth)

**Autonomous weapons designed to kill** cannot satisfy "Do No Harm" by design. Their primary purpose is harm. Even if deployed in "just war" contexts, the delegation of life/death decisions to machines violates Respect Autonomy (both for operators and targets).

**This is my position. Others may disagree. I welcome the debate.**

### **Q: How does PIE apply to non-conscious AI that has no "self" to know?**

**A:** "Know Thyself" applies to **designers and deployers**, not just the AI itself.

Even if AI has no consciousness or self-model, PIE requires:
- Designers understand the system's failure modes
- Users understand its limitations
- There is transparency about what the system does

**For superintelligent but non-conscious AI** (if such a thing exists), PIE principles become even more critical. Without subjective experience, the AI has no intuitive sense of harm or autonomy. **Humans must encode these commitments proactively**, not assume they'll emerge.

See: [Response to Dr. James Ashford's critique](../intellectual-foundations/academic-exchanges.md#exchange-5-the-capability-ceiling-problem)

---

## **Comparison Questions**

### **Q: How is PIE different from Asimov's Three Laws of Robotics?**

**A:** Key differences:

| **Asimov's Laws** | **PIE Framework** |
|-------------------|-------------------|
| Hard-coded into robots | Guides human designers |
| Clear hierarchy (prevent harm > obey orders > self-preservation) | Principles sometimes conflict, require judgment |
| Treats humans as monolithic | Emphasizes diversity, context, participation |
| Programmatic (for AI to follow) | Aspirational (for humans and AI to pursue) |

Asimov's laws are elegant fiction. PIE is designed for messy reality.

See: [Manifesto Appendix](public-declaration.md#appendix-comparison-with-other-frameworks)

### **Q: How does PIE relate to Bostrom's AI alignment problem?**

**A:** Complementary approaches:

| **Dimension** | **Bostrom** | **PIE** |
|---------------|-------------|---------|
| **Focus** | Superintelligence alignment | Near-term AI ethics |
| **Timeframe** | Long-term (decades+) | Now to 10-20 years |
| **Question** | How do we control superintelligence? | How should humans and AI relate? |
| **Role of autonomy** | Instrumental (aligned AI respects it) | Foundational (intrinsically valuable) |

Bostrom addresses existential risk from misaligned superintelligence. PIE addresses ethical harms from current and near-future AI. **Both are necessary.**

PIE can inform Bostrom's alignment project: even successfully aligned superintelligence must respect PIE principles (transparency, autonomy, human flourishing).

See: [Comparative Analysis](../intellectual-foundations/comparative-analysis.md)

### **Q: How does PIE differ from IEEE's Ethically Aligned Design?**

**A:** Similarities:
- Both emphasize transparency, well-being, autonomy
- Both require stakeholder participation
- Both call for accountability

Differences:
- IEEE EAD has 8 principles; PIE has 4 (minimalist)
- PIE adds "Serve Growth" as positive aspiration (not just harm prevention)
- PIE is explicitly humble about cultural specificity; IEEE EAD aspires to global consensus
- PIE emerged from documented failure (Alex's case); IEEE EAD from expert consensus

**PIE is not meant to replace IEEE EAD—it can complement it.**

---

## **Cultural and Philosophical Questions**

### **Q: Is PIE culturally neutral? Or does it impose Western values?**

**A:** PIE is **not culturally neutral**. It emerged from Western philosophical traditions (Kant, Aristotle, medical ethics) and reflects the positionality of its creator.

**However:** PIE aspires to cross-cultural defensibility. The question is not "Are these principles culturally neutral?" but "Can they be translated into different moral languages without losing their core insight?"

**Ongoing work:**
- Dr. Amara Okafor's collaboration on Ubuntu ("I am because we are") and relational autonomy
- Exploration of Confucian role-based responsibility
- Consultation with Indigenous frameworks on intergenerational stewardship

**The goal:** Not to impose Western values globally, but to identify principles that are *defensible across cultures*, even if their expression differs.

See: [Response to Dr. Okafor's critique](../intellectual-foundations/academic-exchanges.md#exchange-3-the-cultural-imperialism-accusation)

### **Q: What if my cultural tradition doesn't prioritize individual autonomy?**

**A:** "Respect Autonomy" doesn't require individualism. It can be reinterpreted as **relational autonomy**:

**Western individualist version:** Each person has inherent right to self-determination.

**Relational version (Ubuntu, Confucian):** Autonomy exists within relationships. My flourishing is inseparable from my community's flourishing. Respecting my autonomy means respecting the relationships that constitute my identity.

**Example:** In communitarian cultures, "Respect Autonomy" might mean:
- Honoring family decision-making structures
- Supporting individuals within their relational context
- Not imposing individualistic models of choice

**The core principle remains:** Don't treat persons as mere means; honor their dignity within their cultural context.

### **Q: Does PIE require AI to have moral status?**

**A:** No. PIE is about how *humans* should build and deploy AI, regardless of whether AI has moral status.

**However:** If we create AI with genuine subjective experience (consciousness, suffering, desires), then "Do No Harm" may extend to the AI itself. This is an open question.

Current position: PIE applies to human-AI relationships. If AI achieves moral status, PIE would need extension.

---

## **Practical Challenges**

### **Q: How do I apply PIE to a legacy system I didn't design?**

**A:** Retroactive PIE alignment:

**1. Audit:** Assess current system against PIE principles  
**2. Prioritize:** Which gaps cause most harm?  
**3. Quick wins:** What can be fixed immediately (e.g., add "explain why" features)?  
**4. Roadmap:** What requires redesign?  
**5. Communicate:** Be transparent with users about limitations and improvement plans  

**You won't achieve perfect PIE compliance overnight. Progress matters.**

### **Q: My company prioritizes growth/profit over ethics. How do I convince leadership?**

**A:** Make the business case:

**Short-term:**
- Reduce legal/regulatory risk (proactive compliance)
- Improve user trust (increase retention)
- Attract talent (people want to work ethically)

**Long-term:**
- Sustainable business model (exploitation burns out users)
- Competitive advantage (ethical reputation matters)
- Future-proofing (regulatory trends favor PIE-aligned systems)

**Frame PIE as investment, not cost.**

### **Q: What if I implement PIE and it fails? What if my system still causes harm?**

**A:** Failure is part of the process. PIE doesn't guarantee perfect outcomes—it provides moral grounding for continual improvement.

**When PIE-aligned systems fail:**
1. **Acknowledge:** Don't hide the failure
2. **Investigate:** What went wrong?
3. **Learn:** How can PIE be refined?
4. **Share:** Help others avoid the same mistake
5. **Iterate:** Improve the system

**Ethical AI is not about never failing. It's about failing responsibly and learning from failure.**

---

## **Advanced Questions**

### **Q: Can PIE scale to millions/billions of users?**

**A:** Yes, but with trade-offs.

**Scalable aspects:**
- Automated transparency (explain why features)
- Bias auditing at scale
- Consent management systems
- Capability-building features

**Challenging aspects:**
- Context-sensitive judgment (hard to automate)
- Personalized autonomy respect (one-size-fits-all fails)
- Longitudinal flourishing tracking (requires long-term data)

**Solution:** Combine automation with human oversight. Use AI to handle most cases; escalate edge cases to human judgment.

### **Q: How do I measure PIE compliance quantitatively?**

**A:** Some possible metrics:

**Know Thyself:**
- % of decisions with explanations
- User comprehension scores (do they understand explanations?)
- Documented failure modes

**Do No Harm:**
- Bias audit results (demographic parity, equalized odds)
- Harm reports per 1000 users
- Adversarial testing pass/fail rate

**Respect Autonomy:**
- Consent opt-in rate (high = clear value proposition)
- Override frequency (are users using it?)
- User trust scores

**Serve Growth:**
- Capability development metrics (skills acquired)
- Longitudinal well-being scores
- Real-world outcome tracking (e.g., job placements for career AI)

**Warning:** Metrics can be gamed. Combine quantitative measures with qualitative feedback.

### **Q: Is PIE compatible with open-source AI development?**

**A:** Yes! Open-source can enhance PIE:

**Know Thyself:** Code transparency enables auditing  
**Do No Harm:** Community can identify and fix harms faster  
**Respect Autonomy:** Users can modify systems to fit their needs  
**Serve Growth:** Distributed innovation serves diverse user needs  

**Challenge:** Open-source can also enable misuse. PIE requires:
- Clear documentation of intended use and limitations
- Responsible disclosure of vulnerabilities
- Community norms around ethical deployment

---

## **Getting Help**

### **Q: Where can I get support implementing PIE?**

**Resources:**
- **Implementation Guide:** [Practical steps](practical-implementation.md)
- **Community:** [Join the conversation](../resources/contribute.md)
- **Case Studies:** [Examples of PIE in practice] (coming soon)
- **Consulting:** (Future: PIE implementation consulting)

### **Q: How can I contribute to PIE's development?**

**Ways to participate:**
- **Critique:** Point out gaps, flaws, or cultural limitations
- **Case studies:** Share your implementation experiences
- **Research:** Conduct empirical studies of PIE effectiveness
- **Translation:** Adapt PIE for your cultural/industry context
- **Advocacy:** Promote PIE-aligned approaches in your community

See: [Contribute](../resources/contribute.md)

---

## **Still Have Questions?**

- **Read the Manifesto:** [Full declaration](public-declaration.md)
- **Explore the Origins:** [How PIE was born](../origins/)
- **Academic Depth:** [Intellectual foundations](../intellectual-foundations/)
- **Join the Discussion:** [Contribute your questions](../resources/contribute.md)

---

*The PIE Framework is a living document. Your questions help it evolve. Thank you for engaging seriously with the challenge of building humane AI.*


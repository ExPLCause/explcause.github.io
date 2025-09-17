---
date: 2025-09-16
categories:
    - Helical
    - Jupyter
    - DSLs
authors:
    - etosch
---

# Jupyter DSLs

One of the broader goals of the [Helical project](/projects.html#helical) is to make writing, maintaining, and debugging experiments easier and safer for the end-user through a novel domain-specific language. However, [learning a new formal language can itself contribute to the difficulty of encoding an experiment](20250917_DSL_usability_reading_list.md). Therefore, we are intersted in mitigating the effects of language learning/novelty. To this end, a Northeastern coop student ([Kevin G. Yang](https://www.linkedin.com/in/kyang004)) investigated the suitability of using Jupyter notebooks as an execution environment for experiments last year.

<!--more-->

Jupyter notebooks are commonly used by empiricists. If we want empiricists to use Helical, then it would make sense to integrate it into empiricists' computational workflow. Kevin began investigating the feasibility of adding such support for features such as syntax highlighting and code completion to Jupyter. This actually turned out to be a surprisingly difficult task!

Kevin ended up doing a deep dive into the Jupyter code base and issue database, resulting in an [experience report](https://kilthub.cmu.edu/articles/conference_contribution/Exploring_Support_for_Lightweight_DSLs_in_Jupyter_Notebooks/29087102) and [tutorial](https://kyang04.github.io/) that he presented internally at the [Northeastern Programming Research Lab's seminar series](https://prl.khoury.northeastern.edu/people.html) and externally at [PLATEAU 2025](https://2025.plateau-workshop.org/program). While his coop focused on a specific implementation task, the work led us to ask new research questions. For example, we were somewhat surprised by the breadth of tooling empirical scientists were using and that there was demand for custom syntax highlight organically in the Jupyter user base &mdash; conventional wisdom in the PL community is that DSLs are a bit niche! Thus, rather than focusing on Helical specifically, we broadened the task to DSL support in Jupyter more generally. 

At the start of his coop, I had envisioned Kevin integrating Helical into Jupyter and then pivoting to a reproduction study. However, as he was working on the project, he became increasingly interested in visualization and usability. We were hoping to perform a user study in Summer 2025 to further investigate some of the research questions that arose and perhaps send a conference paper submission out to CHI or UIST; that [thread was put on hold](https://www.insidehighered.com/news/students/academics/2025/03/11/trumps-cuts-threaten-key-nsf-undergrad-research-program) as Kevin continues [his career exploration journey](https://www.linkedin.com/in/kyang004). 
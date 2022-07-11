# robo_adviser_lite

FinTech Group Project 1

# Guidelines for Project 1

This document contains guidelines, requirements, and suggestions for Project 1.

## Team Effort

First and foremost, remember that projects are a group effort, and working closely with your teammates is a requirement. In addition to learning real-world collaborative workflow, this will allow you to tackle more complex problems than working alone.

In other words, team collaboration helps you to **work smart** and **dream big**. Take advantage of it!

## Project Proposal

Before you start writing any code, your group should outline the scope and purpose of your project. This helps provide direction and prevents [scope creep](https://en.wikipedia.org/wiki/Scope_creep).

Write this as a brief summary of your interests and intent, including:

* The kind of data you'd like to work with and the field you're interested in (e.g., trading, quantitative analysis).

* The kind of questions you'll be asking of that data.

* Possible sources for such data.

This constitutes your Project Proposal and Outline, which should look similar to this:

> Our project is to uncover patterns in credit card fraud. We'll examine relationships between types of transactions and location; purchase prices and times of day; trends in purchases over the course of the year; and related questions, as the data admits.

## Finding Data

Once your group has written an outline, it's time to start hunting for data. You are free to use data from any source, but we recommend the following curated sources of high-quality data:

* [data.world](https://data.world/datasets/canada)

* [Kaggle](https://www.kaggle.com/datasets?search=canada)

* [TSX Stock Exchange](https://www.tsx.com/trading/market-data-and-statistics)

* [Open Data](https://open.canada.ca/en/open-data)

* [Public APIs](https://github.com/abhishekbanthia/Public-APIs)

* [Awesome-APIs List](https://github.com/Kikobeats/awesome-api)

* [Medium APIs List](https://medium.com/@benjamin_libor/a-curated-collection-of-over-150-apis-to-build-great-products-fdcfa0f361bc)

Chances are you'll have to update your Project Outline as you explore the available data. **This is fine**—adjustments like this are part of the process! Just make sure everyone in the group is up to speed on the goals of the project as changes are made.

Make sure that your data is not too large for local analysis. **Big Data** datasets are difficult to manage locally, so consider a subset of that data, or a different dataset altogether.

## Data Cleanup & Analysis

With data in hand, it's time to tackle development and analysis. This is where the fun starts!

Inevitably, the analysis process can be broken into two broad phases: **Exploration and Cleanup** and **Analysis** proper.

As you've learned, you'll need to explore, clean, and reformat your data before you can begin to answer your research questions. We recommend keeping track of these exploration and cleanup steps in a dedicated Jupyter Notebook, both for organization's sake and to make it easier to  present your work later.

Similarly, after you've massaged your data and are ready to start crunching numbers, you should keep track of your work in a Jupyter Notebook dedicated specifically to analysis.

During both phases, **don't forget to include plots**! Don't make the mistake of waiting to build figures until you're preparing your presentation. Creating them along the way can reveal insights and interesting trends in the data that you might not notice otherwise.

We recommend focusing your analysis on techniques such as aggregation, correlation, comparison, summary statistics, and financial analysis.

Finally, be sure that your projects meet the [technical requirements](TechnicalRequirements.md).

## Presentation

After the data is analyzed to satisfaction, assemble a presentation in order to show the work, explain the process, and discuss conclusions.

The presentation will take the form of a slideshow, and should give classmates and instructional staff an overview of your work. PowerPoint, Keynote, and Google Slides are all acceptable for building slides.

As long as the slides meet the [presentation requirements](PresentationRequirements.md), the presentation may be structured however you wish. Many students find the following format helpful [presentation guidelines](PresentationGuidelines.md).

## Submission

In addition to submitting your project on Bootcamp Spot individually, please [fill out this form](https://forms.gle/CBk5tyy4sSsGN8k38) **once per group**.

- - -





# Technical Requirements

The technical requirements for Project 1 are as follows:

* [ ] Use Pandas to clean and format all dataset(s).

* [ ] Create a Jupyter Notebook describing the **data exploration and cleanup** process.

* [ ] Create a Jupyter Notebook illustrating the **final data analysis**.

* [ ] Use Hvplot or GeoViews to create six to eight data visualizations (ideally, at least two per question asked of the data), and aggregate these visualizations into a dashboard.

* [ ] Save PNG images of the visualizations to distribute to the class and instructional team, as well as for the presentation, and your repo's README.md file.

* [ ] Use one new Python library that hasn't been covered in class.

* [ ] Optional: Use at least one API, if an API can be found with data pertinent to your primary research questions.

* [ ] Create a README.md in your repo with a write-up summarizing your major findings. This should include a heading for each question that was asked of your data, with a short description of what you found and any relevant plots under each heading.

# Presentation Requirements

The presentation requirements for Project 1 are as follows:

Each presentation must:

* [ ] Be 8–10 minutes in length (check with the instructor for the official presentation time).

* [ ] Describe the project's core message or hypothesis.

* [ ] Describe the questions the group found of interest, and why.

* [ ] Summarize how, and where, the data was found to answer these questions.

* [ ] Describe the data exploration and cleanup process (accompanied by Jupyter Notebook).

* [ ] Describe the analysis process (accompanied by Jupyter Notebook).

* [ ] Summarize the conclusions. This should include a numerical summary (i.e., what data did the analysis produce), as well as visualizations of that summary (plots of the final analysis data).

* [ ] Discuss the implications of the findings (which shall take the form of an open-ended discussion about what the findings mean).

* [ ] Tell a good story! Storytelling through data analysis is no different than in literature. Find your narrative and use your analysis and visualization skills to highlight conflict and resolution in your data.

## 






# Presentation Guidelines

While you are free to structure your presentation how you like, many people find the following format useful.

* Title Slide

  * Include the name of the project, title of course, group members, and date.

* Motivation & Summary Slide

  * Define the core message or hypothesis of the project.
  * Describe the questions that were asked, and _why_ they were asked.
  * Describe whether the questions were answered to your satisfaction, and briefly summarize the findings.

* Questions & Data

  * Provide more detail on the questions posed, including what kind of data was needed to answer them, and where it was found.

* Data Cleanup & Exploration

  * Describe the exploration and cleanup process.
  * Discuss any insights you had while exploring the data that you didn't anticipate.
  * Discuss any problems that arose after exploring the data, and how they were resolved.
  * Present and discuss interesting figures developed during exploration, ideally with the help of Jupyter Notebook.

* Data Analysis

  * Discuss the steps taken to analyze the data, and answer each question that was asked in your proposal.
  * Present and discuss interesting figures developed during analysis, ideally with the help of Jupyter Notebook.

* Discussion

  * Discuss your findings. Did they meet your expectations, and if not, why? What inferences or general conclusions can be drawn from your analysis?

* Postmortem

  * Discuss any difficulties that arose, and how they were handled.
  * Discuss any additional questions that arose, which couldn't be answered due to time constraints. 
  * What would you research next if you had two more weeks?

* Questions
  * Open-floor Q&A with the audience.


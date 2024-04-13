# Hypothesis Testing in Healthcare: Drug Safety

A pharmaceutical company, GlobalXYZ, recently conducted a randomized controlled drug trial, and this project revolves around the analysis of the dataset obtained from the trial. The primary goal is to assess the safety of the drug under investigation and determine if there are significant adverse reactions associated with it.

## Project Overview

GlobalXYZ has provided us with a dataset from their drug trial, with a specific focus on adverse effects. As a non-profit organization dedicated to drug safety, we are tasked with examining this data to answer important questions regarding the safety of the drug.

## Data Source

The dataset, named `drug_safety.csv`, has been sourced from [Hbiostat](https://hbiostat.org/data/), with the kind permission of the Vanderbilt University Department of Biostatistics. This dataset includes information on various aspects of the drug trial, such as demographic data, vital signs, lab measures, and, most importantly, the presence and severity of adverse effects. 

The dataset is a modified version of the original, with a particular focus on adverse effects and their impact. It contains the following key columns:

- `sex`: Gender of the individual.
- `age`: Age of the individual.
- `week`: The week during which the drug testing occurred.
- `trx`: The treatment group (Drug) or control group (Placebo).
- `wbc`: White blood cell count.
- `rbc`: Red blood cell count.
- `adverse_effects`: Presence or absence of at least one adverse effect.
- `num_effects`: The number of adverse effects experienced by each individual.

## Dataset Proportions

In this dataset, the ratio of drug observations to placebo observations is 2 to 1, allowing us to make a fair assessment of the drug's safety.

## Questions to Explore

We have been assigned a few critical questions to explore and answer based on the dataset. The questions cover various aspects of drug safety and adverse reactions.

## Project Instruction

- Determine if the proportion of adverse effects differs significantly between the Drug and Placebo groups, saving as a variable called two_sample_results containing a test statistic and a p-value.

- Find out if the number of adverse effects is independent of the treatment and control groups, saving as a variable called num_effects_groups containing a test statistic and a p-value.

- Examine if there is a significant difference between the ages of the Drug and Placebo groups, storing the returned test statistic and p-value of your test in a variable called age_group_effects.

## Original Dataset

For reference, the original dataset used in this project can be found [here](https://hbiostat.org/data/repo/safety.rda).

Thank you for joining us on this journey to uncover the safety profile of the drug in question. Our analysis will provide valuable insights into the adverse effects associated with the drug, ultimately contributing to informed decision-making in healthcare.

Let's embark on this data-driven exploration together!
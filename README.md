# clinical-data-profiling
Clinical data quality &amp; exploratory profiling using Python
# Clinical / Health Data Quality & Exploratory Profiling

## Project Overview
This project demonstrates a clinical data quality and exploratory data analysis (EDA) workflow using Python and automated profiling tools. The aim is to assess dataset readiness for downstream analytics, modelling, and governance review in health and research contexts.

The project uses a synthetic Alzheimer’s disease dataset to illustrate best practices in missingness assessment, outlier review, and data type validation.

## Objectives
- Perform an initial clinical data quality assessment
- Identify missingness patterns, outliers, and data type inconsistencies
- Generate a reproducible exploratory profiling report
- Demonstrate governance-aware data analysis practices

## Dataset
- Name: Alzheimers_Synthetic.csv
- Type: Synthetic clinical dataset
- Note: The dataset contains no missing values, consistent with its synthetic nature.

## Tools & Technologies
- Python (pandas, numpy)
- ydata_profiling
- Jupyter / Spyder
- HTML-based automated profiling reports

## Methodology
1. Load and inspect clinical dataset using pandas
2. Perform exploratory profiling using ydata_profiling
3. Review missingness, distributions, correlations, and warnings
4. Document findings relevant to clinical analytics and data governance

## Key Findings
- No missing values detected across variables
- Outliers identified in selected numerical fields
- Minor data type optimisations identified for categorical variables
- Dataset suitable for exploratory and demonstration purposes

## Outputs
- `clinical_data_profile.html` – automated data profiling report
- Python scripts used for data loading and profiling

## Limitations
- Dataset is synthetic and does not fully represent real-world clinical data complexity
- Findings are intended for methodological demonstration only

## Future Enhancements
- Simulate real-world missingness patterns
- Apply clinical rule-based outlier detection
- Integrate with SQL Server or Power BI
- Extend into predictive modelling workflows

## Author
Hong-Cheu Liu

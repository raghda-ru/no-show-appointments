# Investigate a Dataset: No-Show Appointments

## Overview

This project investigates a dataset from Kaggle regarding **no-show appointments** in the healthcare system. The goal is to explore the factors that influence whether patients show up for their scheduled appointments. The dataset includes information about patients, their appointments, and whether they showed up or missed their appointment.

## Table of Contents
1. [Introduction](#Introduction)
2. [Data Wrangling](#Data-Wrangling)
3. [Exploratory Data Analysis (EDA)](#Exploratory-Data-Analysis)
4. [Conclusions](#Conclusions)

---

## 1. Introduction

### Dataset Description
The dataset contains information about patients' scheduled appointments and whether they showed up or missed their appointment. Below are the key columns in the dataset:

- **PatientId**: Unique identifier for each patient.
- **ScheduledDay**: The day the appointment was scheduled.
- **AppointmentDay**: The day the appointment was supposed to take place.
- **Age**: The age of the patient.
- **Gender**: Gender of the patient (Female or Male).
- **Neighbourhood**: The neighbourhood where the hospital is located.
- **Scholarship**: Indicates if the patient is enrolled in a social assistance program (Bolsa Família).
- **Hypertension**: Whether the patient has hypertension.
- **Diabetes**: Whether the patient has diabetes.
- **Alcoholism**: Whether the patient has a history of alcoholism.
- **Handcap**: Whether the patient has any disabilities.
- **SMS_received**: Indicates if the patient received an SMS reminder.
- **No_show**: Indicates whether the patient showed up for their appointment (No = showed up, Yes = missed).

### Questions for Analysis
The analysis aims to answer the following questions:
1. What percentage of patients show up for their appointments, and how many miss their scheduled appointments?
2. Does the likelihood of showing up vary by gender?
3. How do different neighbourhoods influence the likelihood of a patient missing their appointment?
4. What role does having a scholarship (Bolsa Família) play in showing up for appointments?
5. Does the wait time between the scheduled day and the appointment day affect the likelihood of missing an appointment?

---

## 2. Data Wrangling

### Data Loading and Initial Exploration
The dataset was loaded into a Pandas DataFrame using `pd.read_csv()`.

- The dataset contains no missing values (NaN).
- There are no duplicate rows or appointment IDs.

### Data Cleaning
Several steps were taken to clean the data:

1. **Data Type Conversions**:
   - The `PatientId` column was converted from `float` to `int`.
   - The `ScheduledDay` and `AppointmentDay` columns were converted to `datetime`.

2. **Column Name Standardization**:
   - All column names were converted to lowercase and underscores were used instead of hyphens for uniformity.

3. **Handling Outliers**:
   - The "Age" column had a negative value (-1) that was dropped, as it was not realistic.
   - Rows with unreasonable negative values in the "Wait_days" column (calculated as the difference between the appointment date and the scheduled date) were also dropped.

### Key Features
- **Wait_days**: The number of days between when the appointment was scheduled and when it actually took place.
- **No_show**: The target variable indicating whether the patient showed up for their appointment.

---

## 3. Exploratory Data Analysis (EDA)

### Overall Appointment Attendance
A pie chart was plotted to show the proportion of patients who showed up versus those who missed their appointments. Approximately **20.19%** of patients did not show up for their appointments.

### Gender and No-Show Analysis
A count plot was created to compare the no-show rates by gender. The analysis shows that more women show up for their appointments than men.

### Neighbourhood Influence
A count plot showed how appointment attendance varies across different neighbourhoods. The neighbourhood of **"Jardim Camburi"** had the highest number of patients showing up for their appointments.

### Scholarship and No-Show Rates
A count plot was created to compare the no-show rates among patients with and without the **Bolsa Família** scholarship. The analysis suggests that having a scholarship does not significantly influence whether a patient shows up for their appointment.

### Wait Time and No-Show Rates
The number of days between the scheduled and actual appointment date (Wait_days) was computed. A seasonal plot was generated to show how varying wait times affect no-show rates. The analysis revealed that longer wait times generally correlate with higher no-show rates.

---

## 4. Conclusions

### Key Findings
- **20.19% of patients miss their appointments**, while the majority show up.
- **Women are more likely to show up** for their appointments than men.
- The **neighbourhood** in which the hospital is located has an impact on attendance, with certain areas having higher show-up rates.
- The **Bolsa Família scholarship** does not significantly affect appointment attendance, as most patients are enrolled in the program.
- **Wait times**: Longer waits between scheduled and actual appointments tend to lead to higher no-show rates.

### Recommendations for Further Research
- Investigate the impact of other health conditions (such as Hypertension, Diabetes, etc.) on appointment attendance.
- Explore machine learning models to predict no-shows based on the available features (e.g., logistic regression, decision trees, etc.).
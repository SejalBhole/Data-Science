📊 Sales Data Analysis using Python (EDA Project)
=================================================

📌 Project Overview
-------------------

This project performs **Exploratory Data Analysis (EDA)** on a retail sales dataset to uncover meaningful business insights related to customer demographics, purchasing behavior, and product performance.

The analysis includes:

*   Data cleaning and preprocessing
    
*   Handling missing values
    
*   Feature transformation
    
*   Aggregation and grouping
    
*   Data visualization using Seaborn & Matplotlib
    
*   Business insight generation
    

🛠️ Tech Stack
--------------

*   **Python**
    
*   **Pandas**
    
*   **NumPy**
    
*   **Matplotlib**
    
*   **Seaborn**
    
*   **Google Colab / Jupyter Notebook**
    

📂 Dataset Description
----------------------

The dataset contains customer transaction details with the following features:

Column NameDescriptionUser\_IDUnique customer IDCust\_nameCustomer nameProduct\_IDProduct identifierGenderCustomer genderAge GroupAge categoryAgeCustomer ageMarital\_StatusMarital status (0/1)StateCustomer stateZoneGeographical zoneOccupationCustomer occupationProduct\_CategoryCategory of product purchasedOrdersNumber of ordersAmountPurchase amount

🧹 Data Preprocessing
---------------------

The following preprocessing steps were performed:

*   Removed unnecessary columns
    
*   Checked and handled missing values
    
*   Dropped null rows
    
*   Converted data types
    
*   Renamed columns for clarity
    
*   Verified dataset structure using .info() and .describe()
    

Example:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   df.drop(['Status', 'unnamed1'], axis=1, inplace=True)  df.dropna(inplace=True)  df['Amount'] = df['Amount'].astype(int)   `

📊 Exploratory Data Analysis
----------------------------

### 1️⃣ Gender Analysis

*   Female customers are higher in number.
    
*   Total spending by female customers is significantly greater.
    

### 2️⃣ Age Group Analysis

*   Majority of buyers belong to the **26–35 age group**.
    
*   This age group contributes the highest revenue.
    

### 3️⃣ State-wise Analysis

Top states by total orders and sales:

*   Uttar Pradesh
    
*   Maharashtra
    
*   Karnataka
    

These states generate the highest revenue.

### 4️⃣ Marital Status Analysis

*   Married women contribute the highest overall sales.
    

### 5️⃣ Occupation Analysis

*   IT Sector
    
*   Healthcare
    
*   AviationThese occupations show strong purchasing behavior.
    

### 6️⃣ Product Category Analysis

Top performing categories:

*   Food
    
*   Clothing & Apparel
    
*   Electronics
    

Food category generates the highest revenue.

📈 Data Visualization
---------------------

Visualizations were created using:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   sns.countplot()  sns.barplot()  sns.set(rc={'figure.figsize': (15,5)})   `

Bar labels were added for clarity:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   for bars in ax.containers:      ax.bar_label(bars)   `

🔍 Key Business Insights
------------------------

*   Female customers are the primary revenue contributors.
    
*   Customers aged 26–35 form the most active buyer segment.
    
*   Uttar Pradesh leads in total orders and revenue.
    
*   Married women represent a strong purchasing segment.
    
*   Food and Clothing are top-selling product categories.
    

🚀 Project Highlights
---------------------

✔ Clean and structured data analysis workflow✔ Practical implementation of Pandas operations✔ Professional data visualization✔ Real-world business insight extraction✔ Suitable for portfolio and placement interviews

📌 Future Enhancements
----------------------

*   Build an interactive dashboard (Power BI / Tableau)
    
*   Perform predictive sales analysis
    
*   Deploy as a web-based analytics application
    
*   Apply machine learning models for customer segmentation
    

📎 How to Run the Project
-------------------------

1.  Clone the repository
    
2.  pip install pandas numpy matplotlib seaborn
    
3.  Run the Jupyter Notebook / Colab file
    

👩‍💻 Author
------------

**Sejal Pravin Bhole**B.Tech Computer EngineeringMERN Stack Developer | Data Analysis Enthusiast

If you want, I can also generate:

*   🔥 A very attractive GitHub version with badges
    
*   📌 Resume project description (3–4 lines)
    
*   🎯 Interview explanation script
    
*   📁 Proper project folder structure
    

Just tell me 😊
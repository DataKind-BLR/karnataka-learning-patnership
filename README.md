# [Karnataka Learning Partnership](https://klp.org.in/)
The Karnataka Learning Partnership is a non-profit organization working in the education sector. They are trying to help develop a better education platform for children by collecting data through surveys and competition and bring a clearer picture of the current system.

## The Data
KLP holds competition at a Gram Panchayat Level and conducts community surveys with questions to parents about the school and what they think their child knows about the subjects. In addition to this KLP also combines their data with [DISE](http://udise.in/) data, under DISE the government of India collects data of each active school nationwide and contains information about the infrastructure, student ratio, grants, teachers etc. of each school.

We are dealing with 3 data sources : -

    1. Community Feedback
    2. Gram Panchayat Contest Data
    3. DISE

## How [DataKind](http://www.datakind.org/) is helping Karnataka Learning Partnership:

1. Building Visualization Dashboards to easily digest the information. We will be setting up [superset](https://github.com/ApacheInfra/superset).
   Superset is a flexible data exploration tool, that allows users to create, save and share dashboards and also download csv files. It does require some
   basic knowledge of SQL. It also has connectors for a lot of Databases already built upon, which makes it a very mature tool to explore and build upon.

2. Data Analysis and Insights. Exploring how the data can be combined at different levels and how each school/gram panchayat/block/district can be compared.
   Insights related to performance of schools/students

3. Exploration of feasible performance indicators to predict performance of schools/blocks, based on the data provided.

## Results of DataDive

1. We introduced how [Superset](https://github.com/apache/incubator-superset) can be used. Superset is an open source Tool that is used for Exploratory Data Analysis. Details on how to setup and create charts/dashboards in superset can be found in [setup.md](setup.md)
2. We created a formula to measure performance of at any of the levels (District/Block/Village/Gram Panchayat). Details on how to calculate the formula can be found in the [performance_metric.md](performance_metric.md)
3. We introduced an algorithm that can be used to generate ranking at different levels (District/Block/Village/Gram Panchayat/School). The advantage of the algorithm is we can combine multiple metrics to generate the Ranks. More details can be found [Ranking.md](ranking.md).

## Contributors

    @basumpz
    @sach211
    @ShwetanshuSingh
    @heaven00


# 📍 Optimizing Urban Connectivity in Natal-RN

This repository contains all the materials and source code related to a case study on optimizing urban connectivity in Natal, Rio Grande do Norte, Brazil. The project demonstrates how Graph Theory—specifically Minimum Spanning Trees (MSTs) using Kruskal's Algorithm—can be applied to improve the connection between key urban points. In this case, schools were used as reference points within the city of Natal-RN.

### Author: Matheus Bezerra Dantas Saraiva

## 🔗 Links

- 📄 [Article on Medium](https://medium.com/@matheus.saraiva.083/optimizing-urban-connectivity-a-case-study-with-minimum-spanning-trees-in-natal-rn-brazil-a87e193481eb)
- 🧠 [NotebookLM](https://notebooklm.google.com/notebook/b0b8784e-587f-4455-be50-d0c0aa0f582d)
- 🎧 [Audio Summary](https://drive.google.com/file/d/1dYcZXZNEGvvF-s3TK7Em-SJ8xZlB9pAm/view?usp=sharing)

## 📄 Summary

This project explores how Graph Theory and Minimum Spanning Trees (MSTs) can be used to optimize urban connectivity in Natal, Rio Grande do Norte, Brazil. Using Kruskal's Algorithm, we analyzed a network of schools to identify the most efficient connections between them, minimizing total distance while ensuring full network coverage. The project includes code implementation, visualizations, and an article with methodology and results.


## 🗂️ Repository Contents

- `teste.py`: Original Python script used in the study, annotated and commented for clarity.
- `README.md`: This file, explaining the purpose, structure, and usage of the repository.

## ▶️ Running the Project

To replicate the results of this case study, follow these steps:

1. **Clone the Repository**

```bash
git clone https://github.com/mbdsaraiva/optimizing-urban-connectivity-a-case-study-with-minimum-spanning-trees-in-Natal-RN-Brazil.git natal-mst
cd natal-mst

```

2. **Install Dependencies**

Make sure Python is installed. The main libraries required are:

- `osmnx`
- `networkx`
- `matplotlib`

Install them via pip:

```bash
pip install osmnx networkx matplotlib
```

3. **Execute the Script**

Run the following command:

```bash
python teste.py
```

The script will output visualizations of the Minimum Spanning Tree (MST) and display the total optimized network length.

# %%

import numpy as np
df["log_price"] = np.log(df["sale_price"])
df["log_sqft"] = np.log(df["gross_square_feet"] + 1)

df[["sale_price", "gross_square_feet",
    "log_price", "log_sqft"]].describe()

# %%
import seaborn as sns
import matplotlib.pyplot as plt

numeric_cols = ["sale_price", "gross_square_feet"]
corr = df[numeric_cols].corr()

plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f")
plt.title("Correlation Matrix of Key Numerical Variable")
plt.show()

# %%
plt.figure(figsize=(6,4))
sns.scatterplot(x=df["gross_square_feet"], y=df["sale_price"])
plt.title("Sale Price vs Gross Square Feet")
plt.show()

# %%

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor




numeric_features = ["log_sqft"]
categorical_features = ["building_class_8", "borough"]


numeric_transformer = Pipeline(steps=[
    ("scaler", StandardScaler())
])


categorical_transformer = Pipeline(steps=[
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

# ColumnTransformer
preprocess = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)


X = df[numeric_features + categorical_features]
y = df["log_price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model_lr = Pipeline(steps=[
    ("preprocess", preprocess),
    ("lr", LinearRegression())
])

model_lr.fit(X_train, y_train)
lr_r2 = model_lr.score(X_test, y_test)
print("Linear Regression R²:", lr_r2)


# %%


df["sale_date"] = pd.to_datetime(df["sale_date"], errors="coerce")
df["year"] = df["sale_date"].dt.year
df["month"] = df["sale_date"].dt.month
df["month_sin"] = np.sin(2*np.pi*df["month"]/12)
df["month_cos"] = np.cos(2*np.pi*df["month"]/12)

df["log_price"] = np.log(df["sale_price"])
df["log_sqft"] = np.log(df["gross_square_feet"] + 1)

df["sqft_borough_interact"] = df["log_sqft"] * df["borough"].astype("category").cat.codes
df["sqft_class_interact"] = df["log_sqft"] * df["building_class_8"].astype("category").cat.codes

numeric_features = [
    "log_sqft",
    "year",
    "month_sin",
    "month_cos",
    "sqft_borough_interact",
    "sqft_class_interact"
]

categorical_features = ["borough", "building_class_8"]

numeric_transformer = Pipeline(steps=[
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocess = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

X = df[numeric_features + categorical_features]
y = df["log_price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Linear Regression
lr = Pipeline(steps=[
    ("preprocess", preprocess),
    ("lr", LinearRegression())
])
lr.fit(X_train, y_train)
print("LR R²:", lr.score(X_test, y_test))


# %%

coef = lr.named_steps["lr"].coef_
intercept = lr.named_steps["lr"].intercept_

print("Intercept:", intercept)


# %%

ohe = lr.named_steps["preprocess"].named_transformers_["cat"]["onehot"]

ohe_feature_names = ohe.get_feature_names_out(categorical_features)


all_features = numeric_features + list(ohe_feature_names)

print("Total features:", len(all_features))
print(all_features)

coef_df = pd.DataFrame({
    "feature": all_features,
    "coefficient": coef
})



# %%
coef_df["abs_coef"] = coef_df["coefficient"].abs()
coef_df_sorted = coef_df.sort_values("abs_coef", ascending=False)

print(coef_df_sorted)


# %%
import matplotlib.pyplot as plt

topN = 15  
coef_df_sorted.head(topN).plot(
    x="feature", y="coefficient", kind="barh", figsize=(8,6)
)
plt.title("Linear Regression Coefficient Importance")
plt.show()




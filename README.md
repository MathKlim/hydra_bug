# hydra_bug
Recursive instantiation bug with Tensorflow ?

## Step 1 : Create a virtual env

```bash
conda create --name bug python=3.8
```

## Step 2 : Activate your virtualenv and install dependancies

```bash
conda activate bug
```

```bash
pip install -r requirements.txt
```

## Step 3 :

Go at the root of the folder and type :

```python
python src/classifier_bug.py
```

The summary that tensorflow gives of the sequential model should have **two layers** (Dense1 and Dense2) + the Input layer, but there's only one dense layer instead of two.

![bug](bug.png)

The expected behavior should be the following one.

```python
python src/classifier_right.py
```

![expected_behavior](classifier_right.png)
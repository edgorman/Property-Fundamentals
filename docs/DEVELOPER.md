# Developer Notes

1. [How to install the repository](#how-to-install-the-repository)
2. [How to setup the conda environment](#how-to-setup-the-conda-environment)
3. [How to install modules and update the environment](#how-to-install-modules-and-update-the-environment)

* * * * *

## How to install the repository
1. Navigate to a suitable directory

2. Clone the repository:
```
git clone git@github.com:edgorman/Property-Fundamentals.git
```

* * * * *

## How to setup the conda environment
1. Create the conda environment:
```
conda env create --file environment.yml
```

2. Activate the conda environment:
```
conda activate property-fundamentals
```

* * * * *

## How to install modules and update the environment
1. Activate the environment
```
conda activate property-fundamentals
```

2. Install the module by inserting the name in the text below:
```
conda install <module_name>
```

3. Update the environment.yml file in the base directory:
```
conda env export --name property-fundamentals > environment.yml
```

* * * * *

## How to install an updated environment
1. Activate the conda environment
```
conda activate property-fundamentals
```

2. Run the following command:
```
conda env update --file environment.yml --prune
```

# Gym-style API

The domain features a continuos state and a dicrete action space.

The environment initializes:
- cross-sectional dataset with variables X_a, X_s, Y and N observations;
- logit model fitted on the dataset, retrieving parameters \theta_0, \theta_1, \theta_2;

The agent: 
- sees a patient (sample observation);
- predict his risk of admission \rho, using initialized parameters
- if \rho < 1/2:
  - do not intervene on X_a, which stays the same 
- else:
  - sample an action a in [0,1]
  - compute g(a, X_a) = newX_a
  - intervene on X_a by updating it to newX_a
- give reward equal to average risk of admission, using predicted Y, initial parameters and sampled values

(shouldn't I fit a new logit-link? parameters are now diff?)


# To install
- git clone https://github.com/claudia-viaro/gym-contin.git
- cd gym-contin

- !pip install gym-contin
- import gym
- import gym_contin
- env =gym.make('contin-v0')

# To change version
- change version to, e.g., 1.0.7 from setup.py file
- git clone https://github.com/claudia-viaro/gym-contin.git
- cd gym-contin
- python setup.py sdist bdist_wheel
- twine check dist/*
- twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

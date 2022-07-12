{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Homework 7, Part Two: A dataset about dogs.\n",
    "\n",
    "Data from [a FOIL request to New York City](https://www.muckrock.com/foi/new-york-city-17/pet-licensing-data-for-new-york-city-23826/)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Do your importing and your setup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Read in the file `NYC_Dog_Licenses_Current_as_of_4-28-2016.xlsx` and look at the first five rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Owner Zip Code</th>\n",
       "      <th>Animal Name</th>\n",
       "      <th>Animal Gender</th>\n",
       "      <th>Primary Breed</th>\n",
       "      <th>Secondary Breed</th>\n",
       "      <th>Animal Dominant Color</th>\n",
       "      <th>Animal Secondary Color</th>\n",
       "      <th>Animal Third Color</th>\n",
       "      <th>Animal Birth</th>\n",
       "      <th>Spayed or Neut</th>\n",
       "      <th>Guard or Trained</th>\n",
       "      <th>Vaccinated</th>\n",
       "      <th>Application Date</th>\n",
       "      <th>License Issued Date</th>\n",
       "      <th>License Expired Date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10024</td>\n",
       "      <td>BLUE MACK</td>\n",
       "      <td>M</td>\n",
       "      <td>Unknown</td>\n",
       "      <td>AIREDALE TERR</td>\n",
       "      <td>BROWN</td>\n",
       "      <td>BLACK</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2007-11-01</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>2012-09-19 16:01:19.647</td>\n",
       "      <td>2015-09-19</td>\n",
       "      <td>2016-09-19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10461</td>\n",
       "      <td>Indie Zephir</td>\n",
       "      <td>M</td>\n",
       "      <td>Rottweiler</td>\n",
       "      <td>NaN</td>\n",
       "      <td>BLACK</td>\n",
       "      <td>TAN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2013-04-01</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>2013-09-20 11:41:36.647</td>\n",
       "      <td>2014-09-20</td>\n",
       "      <td>2018-09-20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10013</td>\n",
       "      <td>Bilal</td>\n",
       "      <td>M</td>\n",
       "      <td>Australian Cattledog</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Rust</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2014-09-01</td>\n",
       "      <td>Yes</td>\n",
       "      <td>NaN</td>\n",
       "      <td>No</td>\n",
       "      <td>2014-09-12 13:13:36.713</td>\n",
       "      <td>2014-09-12</td>\n",
       "      <td>2019-09-12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>10025</td>\n",
       "      <td>Buddy</td>\n",
       "      <td>M</td>\n",
       "      <td>Unknown</td>\n",
       "      <td>Cockapoo</td>\n",
       "      <td>BLOND</td>\n",
       "      <td>WHITE</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2008-04-01</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>2014-09-12 15:26:51.417</td>\n",
       "      <td>2014-09-12</td>\n",
       "      <td>2017-10-20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>10013</td>\n",
       "      <td>Ali</td>\n",
       "      <td>M</td>\n",
       "      <td>Basenji</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Black</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2014-01-01</td>\n",
       "      <td>No</td>\n",
       "      <td>NaN</td>\n",
       "      <td>No</td>\n",
       "      <td>2014-09-12 15:43:17.707</td>\n",
       "      <td>2014-09-12</td>\n",
       "      <td>2019-09-12</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Owner Zip Code   Animal Name Animal Gender         Primary Breed  \\\n",
       "0           10024     BLUE MACK             M               Unknown   \n",
       "1           10461  Indie Zephir             M            Rottweiler   \n",
       "2           10013         Bilal             M  Australian Cattledog   \n",
       "3           10025         Buddy             M               Unknown   \n",
       "4           10013           Ali             M               Basenji   \n",
       "\n",
       "  Secondary Breed Animal Dominant Color Animal Secondary Color  \\\n",
       "0   AIREDALE TERR                 BROWN                  BLACK   \n",
       "1             NaN                 BLACK                    TAN   \n",
       "2             NaN                  Rust                    NaN   \n",
       "3        Cockapoo                 BLOND                  WHITE   \n",
       "4             NaN                 Black                    NaN   \n",
       "\n",
       "  Animal Third Color Animal Birth Spayed or Neut Guard or Trained Vaccinated  \\\n",
       "0                NaN   2007-11-01            Yes               No        Yes   \n",
       "1                NaN   2013-04-01             No               No        Yes   \n",
       "2                NaN   2014-09-01            Yes              NaN         No   \n",
       "3                NaN   2008-04-01            Yes               No        Yes   \n",
       "4                NaN   2014-01-01             No              NaN         No   \n",
       "\n",
       "         Application Date License Issued Date License Expired Date  \n",
       "0 2012-09-19 16:01:19.647          2015-09-19           2016-09-19  \n",
       "1 2013-09-20 11:41:36.647          2014-09-20           2018-09-20  \n",
       "2 2014-09-12 13:13:36.713          2014-09-12           2019-09-12  \n",
       "3 2014-09-12 15:26:51.417          2014-09-12           2017-10-20  \n",
       "4 2014-09-12 15:43:17.707          2014-09-12           2019-09-12  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_excel(\"NYC_Dog_Licenses_Current_as_of_4-28-2016.xlsx\")\n",
    "df.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## How many rows do you have in the data? What are the column types?\n",
    "\n",
    "If there are more than 30,000 rows in your dataset, go back and only read in the first 30,000.\n",
    "\n",
    "* *Tip: there's an option with `.read_csv` to only read in a certain number of rows*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(81937, 15)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(30000, 15)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_excel(\"NYC_Dog_Licenses_Current_as_of_4-28-2016.xlsx\", nrows = 30000)\n",
    "df.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Describe the dataset in words. What is each row? List two column titles along with what each of those columns means.\n",
    "\n",
    "For example: “Each row is an animal in the zoo. `is_reptile` is whether the animal is a reptile or not”"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Each row contains information registered for a dog/pet. \n",
    "# \"Owner Zip Code\" is the pet owner zip code in NYC.\n",
    "# \"Animal Name\" shows the pet name, and \"Animal Gender\" whether it is male or female. \n",
    "# \"Primary Breed\" indicates which breed a dog is mainly made up of, or if it is unknown.\n",
    "# \"Secondary Breed\" is the the breed a dog might be easily recognizable.\n",
    "# \"Animal Dominant Color\", \"Animal Secondary Color\" and \"Animal Third Color\" is the color of the dog.\n",
    "# \"Animal Birth\" is the date of birth of the dog.\n",
    "# \"Spayed or Neut\" is whether the dog is dterilized or not.\n",
    "# \"Guard or Trained\" is whether or not the dog is trained.\n",
    "# \"Vaccinated\". is whether or not the dog is vaccinated.\n",
    "# \"Application Date\" is the date in which the owner submitted an application to register their dog\n",
    "# \"License Issued Date\" and \"License Expired Date\" is the date in which the license was issued \n",
    "# and the date in which it expires"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Your thoughts\n",
    "\n",
    "Think of four questions you could ask this dataset. **Don't ask them**, just write them down in the cell below. Feel free to use either Markdown or Python comments."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# What are the most common names and how does it change by NYC areas?\n",
    "# Are dogs with unknown \"Primary Breed\" more common on certain NYC areas? Where \n",
    "# are purebreds more common? What are the most popular breeds and how does that change by area?\n",
    "# Are purebreds more likely to not been vaccinated?\n",
    "# Are there breeds that are more likely to be trained?\n",
    "# Unique dog of a certain breed in NYC?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Looking at some dogs"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What are the most popular (primary) breeds of dogs? Graph the top 10."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Unknown                                 4777\n",
       "Yorkshire Terrier                       1882\n",
       "Shih Tzu                                1760\n",
       "Chihuahua                               1535\n",
       "Maltese                                 1133\n",
       "Labrador Retriever                      1074\n",
       "American Pit Bull Terrier/Pit Bull       780\n",
       "Labrador Retriever Crossbreed            738\n",
       "American Pit Bull Mix / Pit Bull Mix     722\n",
       "Jack Russell Terrier                     553\n",
       "Name: Primary Breed, dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Primary Breed'].value_counts().head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## \"Unknown\" is a terrible breed! Graph the top 10 breeds that are NOT Unknown\n",
    "\n",
    "* *Tip: Maybe you want to go back to your `.read_csv` and use `na_values=`? Maybe not? Up to you!*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(30000, 15)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_excel(\"NYC_Dog_Licenses_Current_as_of_4-28-2016.xlsx\", nrows = 30000, na_values = \"Unknown\")\n",
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAg4AAAD4CAYAAACE724UAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAAsTAAALEwEAmpwYAAAs4UlEQVR4nO3de7hd073/8fdHkCCkCBqhtmqUtIhkizuJpnEtVbQ8VELbnPRpqfZHmx6qcXqRlraotpE6BNXGCaopPcQlIS6R7Fy3RFBN9Ah1F+JW4vv7Y47FzLLX2nNf1058Xs+znz3nmGOM+Z1z7WR+1xhjr62IwMzMzKyIdWodgJmZma05nDiYmZlZYU4czMzMrDAnDmZmZlaYEwczMzMrbN1aB2DW0Xr37h11dXW1DsPMbI0yZ86c5yNii/JyJw621qurq6OhoaHWYZiZrVEkPdFUuacqzMzMrDAnDmZmZlaYEwczMzMrzImDmZmZFebFkbbWa1y+groxt9Q6jA+NZeMOr3UIZtaBPOJgZmZmhTlxsDaRtErSfEkLJM2VtE8HnGOspDPbu18zM2s5T1VYW70REQMAJB0MnA8cWNOIzMysw3jEwdrTJsBLpR1JZ0maLWmhpPNy5TdJmiNpkaRRufKvSHpU0ixJv5d0afkJJO0g6dbUfoaknTr8qszM7D0ecbC22kDSfKAH0Ac4CEDScKAfMBgQMEXSARFxD3BqRLwoaQNgtqQbgO7AD4CBwKvAXcCCJs43ARgdEY9J2hP4bemceSkhGQXQbZMPfGKqmZm1khMHa6v8VMXewNWSPg0MT1/zUr2eZInEPcDpko5O5dum8o8Cd0fEi6mvycCO+RNJ6gnsA0yWVCru3lRQETGBLMmge59+0earNDMzwImDtaOIeEBSb2ALslGG8yPisnwdSUOAYcDeEfG6pOlkoxVFrAO8XEpUzMys83mNg7WbtN6gG/ACcBtwaholQFJfSVsCvYCXUtKwE7BXaj4bOFDSppLWBY4p7z8iXgGWSjou9SlJu3X4hZmZ2Xs84mBtVVrjANkow4iIWAVMlbQz8ECaVlgJnATcCoyW9DDwCDATICKWS/opMAt4EVgCrGjifCcCv5N0DrAeMImm10KYmVkHcOJgbRIR3aocuxi4uIlDh1Zo8seImJBGHP4M3JT6GZvrcylwSGvjNTOztnHiYF3JWEnDyNY8TCUlDm21S99eNPhjkM3M2oUTB+syIsKfDmlm1sV5caSZmZkV5sTBzMzMCnPiYGZmZoU5cTAzM7PCnDiYmZlZYU4czMzMrDAnDmZmZlaYEwczMzMrzImDmZmZFeZPjrS1XuPyFdSNuaXWYXzoLPPHfJutlTziYGZmZoU5ceggkla2os1ESccWqLNU0nxJCyR9pvVRFo5riKSb0/ZISZeWHT8lxTNf0r8lNabtca08398kfaQdQjczs3bmqYo101kRcb2kocAEoF8tg4mIK4ErASQtA4ZGxPPNtZMkQBHxbtn+YS05v6RuEbGqxYGbmVmLecShA0nqKelOSXPTu/CjcsdOlrQwjRpc00TbH6XRhW5VTvEA0DfVX20kQNLNaaSgW+rnoRTDt9Px0yUtTjFMSmUbSbpC0ixJ8/LxtvL6z5I0O53jvFRWJ+kRSVcDDwH7l+1vK2mZpN6p/kkpnvmSLivdD0krJf1C0gJg77bEaWZmxXnEoWO9CRwdEa+kB+FMSVOA/sA5wD4R8bykzfKNJF0AbAycEhFRpf9DgJuaiWEA0DciPp36/kgqHwNsHxFv5crOBu6KiFNT2SxJdxS60jKShpONhAwGBEyRdADwz1Q+IiJmSqrL76e2pT52Br4E7BsRb0v6LXAicDWwEfBgRPy/CucfBYwC6LbJFq25BDMza4ITh44l4Kfpgfku2ejAVsBBwOTScH5EvJhr8wOyB+KoKv1eIOmnwDY0/277H8DHJf0auAWYmsoXAtdKuon3k4/hwJGSzkz7PYCPNXeRFQxPX/PSfk+yBOGfwBOlJCEp3y/5DDAImJ2SiQ2AZ9OxVcANlU4eERPIpnHo3qdfteTLzMxawIlDxzoR2AIYlN4xLyN7GFczGxgkabOyhCKvtMbhNOAKsofrO6w+9dQDICJekrQbcDAwGvgicCpwOHAA8DngbEm7kCU6x0TEI/mTSdqq6AXnmwHnR8RlZX3VAa+V1S3fz/dxVUR8v4ljb3pdg5lZ5/Mah47VC3g2JQ1Dge1S+V3AcZI2ByibqrgVGAfcImnjZvq/FFhH0sHAMmCApHUkbUs2RUCaIlknIm4gmx4ZKGkdYNuImAZ8L8XZE7gNOC0tUkTS7m249tuAUyX1TH31lbRlC/u4Ezi21E7SZpK2a6aNmZl1II84dABJ6wJvAdcCf5XUCDQASwAiYpGknwB3S1pFNpw/stQ+IianpGGKpMMi4o2mzhMRIenHwHeBYcBSYDHwMDA3VesLXJmSBYDvA92AP0jqRfau/pKIeFnSj4CLgIWp/lLgiNbcg4iYmtYoPJDykJXASWRTDEX7WCzpHGBqiudt4BvAE62JyczM2k7V195Za6Spgd9HxOBax2JQX18fDQ0NtQ7DzGyNImlORNSXl3uqop1JGg38iWxawMzMbK3iqYp2FhHjgfG1jsPMzKwjeMTBzMzMCnPiYGZmZoU5cTAzM7PCnDiYmZlZYU4czMzMrDAnDmZmZlaYEwczMzMrzImDmZmZFeYPgLK1XuPyFdSNuaXWYVgHWzbu8FqHYPah4BEHMzMzK8yJg5mZmRVWKHGQ9HlJIWmnjgpEUr2kSzqw/yGSVkiaL+lhST9M5aMlnZy2R0raukL7iZKWpvZLSu2bOedISZem7bGSzmyizth0bz+RKzsjldWn/b9J+kgLr3e8pH2bONfydA0PSToylV8uqX/a/s8qfS6T1JjaN0o6qkAcEyUdm7anl66prM50Sf9U+vvbqewmSSvT9taSri967WZm1nGKjjicANybvrc7SetGRENEnN4R/efMiIgBQD1wkqSBETE+Iq5Ox0cCTSYOyVmp/QBghKTt2ymuRuD43P5xwKLSTkQcFhEvt7DPvYCZTZT/Kl3DccAVktaJiK9GxOJ0vGLikAxN7Y8F2jPRexnYFyAlSX1KByLiqYg4th3PZWZmrdRs4iCpJ7Af8BVyD7f0Dv5uSX+R9A9J4ySdKGlWeje6Q6q3haQbJM1OX6WHw1hJ10i6D7gm9Xdz6ZySrkz9LJR0TCr/naQGSYsknZeLZZmk8yTNTW2qjoxExGvAHOATpZGA9K64Hrg2vaPeoEoXPdL313Ln75226yVNb+6+lrkJOCq13wFYATxfdn29Je2R7kcPSRul+/Dp8s4k7Qw8GhGrKp0wIh4G3gF6l0YCJI0DNkjXf20zMW8CvJTOVyfpodz5z5Q0tuC1l0zi/Z+vLwA35vp7r39J35Z0RdreJY2cbNjCc5mZWSsVGXE4Crg1Ih4FXpA0KHdsN2A0sDPwZWDHiBgMXA6clupcTPYudw/gmHSspD8wLCLKRzJ+AKyIiF0iYlfgrlR+dkTUA7sCB0raNdfm+YgYCPwO+MCUQJ6kzcnekeff1V8PNAAnRsSAiHijiaYXSJoPPAlMiohnq52nBV4B/i8lAccD1zVVKSJmA1OAHwM/B/4QEQ81UfVQ4NZqJ5S0J/Au8Fyu/zHAG+n6T6zQdFp6iN8NnFP1qlrmTuAASd2ocg/Ifp4+Ielo4ErgPyLi9fJKkkalJLNh1esr2jFMM7MPtyKJwwlk7wZJ3/MP+dkR8XREvAU8DkxN5Y1AXdoeBlyaHrhTgE3SKAbAlAoP6GHAb0o7EfFS2vyipLnAPOBTZIlHSekd6pzcucvtL2leinNcRCyqUK+S0lTFR4HPSNqnhe2rKb3j/jzw5yr1/gv4LNnoyM8r1DmYyonDt9NrcSHwpYiIFsY5NCI+DexC9rr2bK5BQavIpsOOBzaIiGVNVYqId8mmlK4B7o6I+yrUmxAR9RFR323DXu0UopmZVf0cB0mbAQcBu0gKoBsQks5KVd7KVX83t/9uru91gL0i4s2yviEN9ReR1hOcCewRES9Jmsj7Uwb5WFZVua4ZEXFE0XNWEhEr03TEfsD9ZEP+pSSsR6V2zbgZuABoiIhXcusEy20O9ATWS+da7R6mYfuPRMRTFdr/KiIubGWM74mIxyU9Q5a8PcXqSWhr78EksqRpbDP1+gErqb4exczMOkBzIw7HAtdExHYRURcR2wJLgf1bcI6pvD9tgaQBBdrcDnwj12ZTsjn114AVkrYiG45vb68CGzdXSdK6wJ5koywAy4DSFM4xrTlxGm7/HvCTZqpeRjaVcy3wsyaODwWmtSaG5G1J6zVXSdKWwPbAE8AzwJaSNpfUHWhtcjYDOB/4U5Xz9iJblHkAsHlam2JmZp2kucThBD44bH4DLfvtitOB+rSobzHZmojm/BjYNC18W0A2PL6AbIpiCfBHoMkh6jaaCIyvsjiytMZhIdl0TGl65DzgYkkNZCMerRIRkyJibqXjyn5t9O2I+CMwDthD0kFl1Zpd39CMCcDCKosjp6V7MA0YExHPRMTbZFMos8iSviWtOXFkLoyI56tU+xXwm7Tm5ivAuJTEmJlZJ1DLp7itK0trQPZMD3MD6uvro6GhodZhmJmtUSTNSb+QsBr/rYq1TPrNEjMzsw7hj5w2MzOzwpw4mJmZWWFOHMzMzKwwJw5mZmZWmBMHMzMzK8yJg5mZmRXmxMHMzMwKc+JgZmZmhTlxMDMzs8L8yZG21mtcvoK6MbfUOgzrRMvGHV7rEMzWWh5xMDMzs8I6LXGQtLIFdcdKOrMdzz1S0qVtaD9E0or0VzOXSLqwQJszJG1Y5fjlkvq3NqbWkHRy+oujjZLmtec9LjtPm+53VzuPmZm9b40dcZDUYdMsFfqeEREDgN2BIyTt20w3ZwBNJg6SukXEVyNicZsCrUJSt7L9Q1NMwyNiF2AvYEUT7Tpl+kqZNfbnz8zsw6qm/3FL+pykB9O73zskbZU7vJukByQ9Julrqf4QSTMkTQEWp7KbJM2RtEjSqFzfp0h6VNIsYN9ceZ2kuyQtlHSnpI+l8omSxkt6EPh5pZgj4g1gPtA3tRue4pwrabKknpJOB7YGpkmaluqtlPQLSQuAvSVNl1RfpY9DJE3OxT1E0s2V6qfyZZJ+lv609nFloX8fODMinkrX8VZE/D61my7pIkkNwLckfSa9Jo2SrpDUPdUbJ2lxuncXprLj0ijGAkn35M63ber3MUk/zN37RyRdDTyU6pwlaXbq87zc9Z4kaVYa5bmslAhVel3NzKxz1Pod373AXhGxOzAJ+G7u2K7AQcDewLmStk7lA4FvRcSOaf/UiBgE1AOnS9pcUh/gPLIHy35Afkrg18BVEbErcC1wSe7YNsA+EfGdSgFL2hToB9wjqTdwDjAs/TnrBuA7EXEJ8BQwNCKGpqYbAQ9GxG4RcW+uvyb7AO4A9pS0Uar6JWBSlfolL0TEwIiYVBb6p4E5la4LWD/93fXfABOBL6WRiXWBr0vaHDga+FS6dz9O7c4FDo6I3YAjc/0NBo4hex2PKyVJ6d79NiI+BXwy7Q8GBgCDJB0gaed0vfumUZ5VwInNvK6rkTRKUoOkhlWvf2BgxczMWqnWv1WxDXBdeiCsDyzNHftLenf/RnrXPhh4GZgVEfl6p0s6Om1vS/Yg+igwPSKeA5B0HVBKNPYGvpC2r2H10YXJEbGqQqz7p9GCfsBFEfEvSUeQPbzuk0S6hgcqtF8F3NBE+V5N9RER70i6FficpOuBw8kSqwObOed1Fc7fnFK7TwJLI+LRtH8V8A3gUuBN4L/TyMfN6fh9wERJ/wPcmOvv9oh4AUDSjWQP+puAJyJiZqozPH3NS/s9ye7vrsAgYHa6xg2AZ4E9qfy6riYiJgATALr36RctvBdmZlZBrROHXwO/jIgpkoYAY3PHyv+zL+2/VipIbYYBe0fE65KmAz3aEM9rVY7NiIgjJG0PzEwPSpE9IE8o0PebFZKSan1MAr4JvAg0RMSryp6k1c5Z6RoWkT2M72phOwBSIjMY+AxwbIrroIgYLWlPssRmjqRBpSblXTRxHgHnR8Rl+YqSTiMbFfp+Wfnnq8VoZmYdr9ZTFb2A5Wl7RNmxoyT1SEPkQ4DZFdq/lJKGncjevQM8CByYpi3WY/X5/vuB49P2icCMlgScRjvGAd8DZgL7SvoEgKSNJJXeAb8KbFygy2p93E02NfM1siSiufrVnA9cIOmjqd36kr7aRL1HgLpS/8CXgbvTOopeEfE34NvAbqmfHSLiwYg4F3iObNQH4LOSNpO0AfB5spGJcrcBp+bWaPSVtCVwJ3Bs2ib1sx3VX1czM+sEnTnisKGkJ3P7vyQbYZgs6SWyd8Lb544vBKYBvYEfRcRTTTwgbwVGS3qY7IE3EyAinpY0lmwI/2WyxYwlpwFXSjqL7EF3SiuuZTxwJtm6hZHAn0oLCMnWHzxKNkx+q6SncuscPiAinpPUZB8RsSpNC4wkJVbV6lcLOCL+pmzx6R1p1CKAK5qo96akU8hel3XJErbxwGbAXyT1IBspKK2ruEBSv1R2J7CAbL3CLLKpmW2AP0REg6S6snNNTesZHkhTEiuBkyJisaRzgKnKfvPibeAbETGzyutqZmadQBGe/rW1W/c+/aLPiItqHYZ1In9ypFnbSZqTFs2vptZrHMw63C59e9HgB4mZWbuo9RoHMzMzW4M4cTAzM7PCnDiYmZlZYU4czMzMrDAnDmZmZlaYEwczMzMrzImDmZmZFebEwczMzApz4mBmZmaFOXEwMzOzwvyR07bWa1y+groxt9Q6DOsi/HcszNrGIw5mZmZWWIclDpI+Lykk7dSB56iXdEkH9j9E0gpJ8yU9LOmHqXy0pJPT9khJW1doP1HS0tR+Sal9M+ccKenStD1W0pllx89O/c2XtCq3fXorr/H+VrYbI+nEFOPyFMNDko5Mxy+X1D9t/2eVfpZJakztGyUdVeDcEyUdm7anS/rAX28zM7OO0ZEjDicA96bv7U7SuhHREBGtemC2wIyIGADUAydJGhgR4yPi6nR8JNBk4pCcldoPAEZI2r4twUTETyJiQOrzjdJ2RFRNoCSt29R+ROxT9NzKlH5mDgampu1fpXiOA66QtE5EfDUiFqfjFROHZGhqfyzQYYmgmZm1XYckDpJ6AvsBXwGOz5UPkXS3pL9I+oekceld66z0bnOHVG8LSTdImp2+9k3lYyVdI+k+4JrU382lc0q6MvWzUNIxqfx3khokLZJ0Xi6WZZLOkzQ3tak6MhIRrwFzgE+URgLSu9564Nr0jnmDKl30SN9fy52/d9qulzS98A0uI6mbpAvSvVoo6T9S+RBJMyRNARaX76c6K3P9nJXr47xUVifpEUlXAw8B20raBFg/Ip4ru0cPA+8AvUsjAZLGARuk+3NtM5eyCfBS7rwP5WI7U9LY1t4jMzNrHx014nAUcGtEPAq8IGlQ7thuwGhgZ+DLwI4RMRi4HDgt1bmY7F3sHsAx6VhJf2BYRJSPZPwAWBERu0TErsBdqfzsiKgHdgUOlLRrrs3zETEQ+B1wJlVI2hzYC1hUKouI64EG4MT0rv+NJppeIGk+8CQwKSKerXaeVvoK2bXvAewBfC03sjEQ+FZE7FhhHwBJw4F+wGCy0ZFBkg5Ih/sBv42IT0XEE8Aw4M7yICTtCbwLvJdQRMQY3h8ZObFC/NNSknA3cE7LLr1pkkalhLFh1esr2qNLMzOj436r4gSyhz/ApLQ/J+3PjoinASQ9zvvD3Y3A0LQ9DOgvqdTfJmkUA2BKhQf0MHKjGxHxUtr8oqRRZNfahyzxWJiO3Zi+zwG+UOFa9pc0j+yBOC4iFkk6rtKFN+GsiLg+xX+npH0iolXrCqoYDuxamvcHepE97P8NzIqIpbm65fv5PoYD89J+z9THP4EnImJmru4hwJW5/W9LOgl4FfhSRETutStiaEQ8n0ac7mzL6EtJREwAJgB079Mv2tqfmZll2j1xkLQZcBCwi6QAugEh6axU5a1c9Xdz++/m4lkH2Csi3izrG9JQf8FYticbSdgjIl6SNJH3pwzysayi8r2YERFHFD1nJRGxMj0Q9wPuJxvSL4349KjUriABp0XEbasVSkP44P2qdP8EnB8Rl5X1UddEm8HA13P7v4qIC1sW8gdFxOOSniFL7p5i9RGxtt4jMzNrBx0xVXEscE1EbBcRdRGxLbAU2L8FfUzl/WkLJA0o0OZ24Bu5NpuSzZm/BqyQtBVwaAtiKOpVYOPmKqXFiHsCj6eiZUBpCueYNsZwG/B1Seulc+0oaaNW9HFqaWRHUl9JW5ZXkvQpYElErGpB32+XYqsmnW974AngGWBLSZtL6g60OXkzM7O264jE4QTgz2VlN9Cy3644HahPi/QWk62JaM6PgU2V/UrgArLh7wVkQ+9LgD8C97UghqImAuOrLI4srXFYSDYdU5oeOQ+4WFID2YhHW1xOtthxblorcBktHE2KiKlk9+gBSY3A9TSdEB0K3NrC+CYAC6ssjpyW7tE0YExEPBMRbwP/BcwiSwqXtPCcZmbWARTh6V8rTtLtwMmldSprgu59+kWfERfVOgzrIvzJkWbFSJqTfrlgNf7IaWuRiPhsrWNoqV369qLBDwszs3bhj5w2MzOzwpw4mJmZWWFOHMzMzKwwJw5mZmZWmBMHMzMzK8yJg5mZmRXmxMHMzMwKc+JgZmZmhTlxMDMzs8KcOJiZmVlh/shpW+s1Ll9B3Zhbah2GWbvy39ywWvGIg5mZmRXmxKEDSFrZgrpjJZ3ZjuceKenSNrQfImlF+jPhSyRdWKDNGZI2rHL8ckn9WxuTmZl1HU4c1gCSOmxKqULfMyJiALA7cISkfZvp5gygycRBUreI+GpELG5ToFVI6tZRfZuZ2eqcOHQSSZ+T9KCkeZLukLRV7vBukh6Q9Jikr6X6QyTNkDQFWJzKbpI0R9IiSaNyfZ8i6VFJs4B9c+V1ku6StFDSnZI+lsonShov6UHg55Vijog3gPlA39RueIpzrqTJknpKOh3YGpgmaVqqt1LSLyQtAPaWNF1SfZU+DpE0ORf3EEk3V6qfypdJ+pmkucBxrXxZzMyshZw4dJ57gb0iYndgEvDd3LFdgYOAvYFzJW2dygcC34qIHdP+qRExCKgHTpe0uaQ+wHlkCcN+QH5K4NfAVRGxK3AtcEnu2DbAPhHxnUoBS9oU6AfcI6k3cA4wLCIGAg3AdyLiEuApYGhEDE1NNwIejIjdIuLeXH9N9gHcAewpaaNU9UvApCr1S16IiIERMamJ2EdJapDUsOr1FZUu0czMWsi/VdF5tgGuSw/69YGluWN/Se/u30jv2gcDLwOzIiJf73RJR6ftbcke6h8FpkfEcwCSrgNKicbewBfS9jWsProwOSJWVYh1/zRa0A+4KCL+JekIsqTkPkmka3igQvtVwA1NlO/VVB8R8Y6kW4HPSboeOJwssTqwmXNeV+H8RMQEYAJA9z79olI9MzNrGScOnefXwC8jYoqkIcDY3LHyB1tp/7VSQWozDNg7Il6XNB3o0YZ4XqtybEZEHCFpe2CmpP8BBNweEScU6PvNCklJtT4mAd8EXgQaIuJVZdlCtXNWuwYzM+sAnqroPL2A5Wl7RNmxoyT1kLQ5MASYXaH9Sylp2Ins3TvAg8CBadpiPVaf778fOD5tnwjMaEnAabRjHPA9YCawr6RPAEjaSFJpZONVYOMCXVbr426yqZmvkSURzdU3M7MacOLQMTaU9GTu6ztkIwyTJc0Bni+rvxCYRvag/FFEPNVEn7cC60p6mOxhPhMgIp5OfT8A3Ac8nGtzGnCKpIXAl4FvteJaxgMHkK1bGAn8KfX3ALBTqjMBuLW0OLKSNJ3SZB9phOJm4ND0vWp9MzOrDUV4+tfWbvX19dHQ0FDrMMzM1iiS5kREfXm5RxzMzMysMCcOZmZmVpgTBzMzMyvMiYOZmZkV5sTBzMzMCnPiYGZmZoU5cTAzM7PCnDiYmZlZYU4czMzMrDAnDmZmZlaY/zqmrfUal6+gbswttQ7DrCaWjTu81iHYWsYjDmZmZlaYEwczMzMrzImDtYikkPSH3P66kp6TdHMz7YaU6qTtfTo6VjMza39OHKylXgM+LWmDtP9ZYHkL+xgCOHEwM1sDOXGw1vgbUFpxdQLwp9IBSYMlPSBpnqT7JX0y31BSHTAa+Lak+ZL2l7SFpBskzU5f+6a6B6Y681N/G6fys1K9hZLO64wLNjOzjBMHa41JwPGSegC7Ag/mji0B9o+I3YFzgZ/mG0bEMmA88KuIGBARM4CL0/4ewDHA5an6mcA3ImIAsD/whqThQD9gMDAAGCTpgPIAJY2S1CCpYdXrK9rnqs3MzL+OaS0XEQvTyMEJZKMPeb2AqyT1AwJYr0CXw4D+kkr7m0jqCdwH/FLStcCNEfFkShyGA/NS3Z5kicQ9ZTFOACYAdO/TL1p2hWZmVokTB2utKcCFZOsVNs+V/wiYFhFHp+RieoG+1gH2iog3y8rHSboFOAy4T9LBgIDzI+KytoVvZmat4akKa60rgPMiorGsvBfvL5YcWaHtq8DGuf2pwGmlHUkD0vcdIqIxIn4GzAZ2Am4DTk0jEkjqK2nLtl2KmZkV5cTBWiUinoyIS5o49HPgfEnzqDyi9Vfg6NLiSOB0oD4tdlxMtngS4AxJD0laCLwN/G9ETAX+CDwgqRG4ntWTEDMz60CK8PSvrd3q6+ujoaGh1mGYma1RJM2JiPryco84mJmZWWFOHMzMzKwwJw5mZmZWmBMHMzMzK8yJg5mZmRXmxMHMzMwKc+JgZmZmhTlxMDMzs8KcOJiZmVlhThzMzMysMP91TFvrNS5fQd2YW2odhpl1AcvGHV7rENZ4HnEwMzOzwpw4fAhJ+qikSZIelzRH0t8kjZJ0c4X6l0vqn7ZXtlMMdZIeao++zMys83iq4kNGkoA/A1dFxPGpbDfgyEptIuKrnRSemZl1cR5x+PAZCrwdEeNLBRGxAJgB9JR0vaQlkq5NSQaSpkt670+rSvqJpAWSZkraKpVNlHRsrs7K9L2npDslzZXUKOmoXCzdJP1e0iJJUyVtUH4+Sb0lLUvbdZJmpL7mStqng+6RmZlV4MThw+fTwJwKx3YHzgD6Ax8H9m2izkbAzIjYDbgH+Foz53sTODoiBpIlLb8oJSRAP+A3EfEp4GXgmGb6ehb4bOrrS8AllSqmqZcGSQ2rXl/RTLdmZlaUEwfLmxURT0bEu8B8oK6JOv8GSmsh5lSokyfgp5IWAncAfYGt0rGlETG/BX2tB/xeUiMwmSzBaVJETIiI+oio77Zhr2a6NTOzorzG4cNnEXBshWNv5bZX0fTPx9sREU3UeYeUiEpaB1g/lZ8IbAEMioi307RDjwrn26C8r1xdgG8DzwC7peNvVrgOMzPrIB5x+PC5C+guaVSpQNKuwP5t7HcZMChtH0k2OgDQC3g2JQ1Dge1a2Fc+yekFPJ1GRL4MdGtjzGZm1kJOHD5k0mjB0cCw9OuYi4DzgX+1sevfAwdKWgDsDbyWyq8F6tP0wsnAkgJ9XQh8XdI8oHeu/LfAiHSOnXLnMDOzTqL3R53N1k7d+/SLPiMuqnUYZtYF+JMji5M0JyLqy8u9xsHWerv07UWD/7MwM2sXnqowMzOzwpw4mJmZWWFOHMzMzKwwJw5mZmZWmBMHMzMzK8yJg5mZmRXmxMHMzMwKc+JgZmZmhTlxMDMzs8KcOJiZmVlh/shpW+s1Ll9B3Zhbah2GmVlFa9Lf0PCIg5mZmRXmxMGqknS2pEWSFkqaL2nPVL5MUu8m6h8paUzanijp2Cp9b576nC/pX5KW5/bX77irMjOz1vJUhVUkaW/gCGBgRLyVEoWqD/SImAJMKdJ/RLwADEjnGgusjIgL2xKzmZl1LI84WDV9gOcj4i2AiHg+Ip7KHT9N0lxJjZJ2ApA0UtKluToHSLpf0j+qjT6UkzQ6N/qwVNK0VL4yV+dYSRPbcoFmZtYyThysmqnAtpIelfRbSQeWHX8+IgYCvwPOrNBHH2A/spGLcUVPHBHjI2IAsAfwJPDLlgQuaZSkBkkNq15f0ZKmZmZWhRMHqygiVgKDgFHAc8B1kkbmqtyYvs8B6ip0c1NEvBsRi4GtWhHGxcBdEfHXljSKiAkRUR8R9d027NWK05qZWVO8xsGqiohVwHRguqRGYAQwMR1+K31fReWfpbdy22rJuVOSsh3wzXxIue0eLenPzMzaziMOVpGkT0rqlysaADzRSeceRDb9cVJEvJs79IyknSWtAxzdGbGYmdn7POJg1fQEfi3pI8A7wN/Jpi06wzeBzYBpkgAaIuKrwBjgZrKpk4YUo5mZdRJFRPO1zNZg3fv0iz4jLqp1GGZmFXXFT46UNCci6svLPeJga71d+vaioQv+ozQzWxN5jYOZmZkV5sTBzMzMCnPiYGZmZoU5cTAzM7PCnDiYmZlZYU4czMzMrDAnDmZmZlaYEwczMzMrzImDmZmZFeZPjrS1XuPyFdSNuaXWYZiZdaqO+hhrjziYmZlZYU4czMzMrDAnDl2EMvdKOjRXdpykWwu0HSnp0oLnqVhX0t/Sn9BuMUkPSpov6Z+Snkvb8yXVtaKvIyWNaU0cZmbWsbzGoYuIiJA0GpgsaRrZa/NT4JBq7SS122sYEYc10b/I/vz6u8203TPVHwnUR8Q3i5xT0roR8U7Z/hRgStG4y/swM7OO48ShC4mIhyT9FfgesBHwB+AXkj4OvA6MioiFksYCOwAfB/4J3FbqQ9LhwDnA54ChwA+BVcCKiDggVds6jWTsAPw5Ir6b2i4D6oGeqc8HgUHAYZK+CHwR6J7a/LC565G0A/AbYIsU/9ciYomkicCbwO7AfZI2K9tfSEo+JG0BjAc+lro9IyLua+IenND8HTYzs7Zy4tD1nAfMBf4N3AvMi4jPSzoIuBoYkOr1B/aLiDfSu3wkHQ18BzgsIl6SdC5wcEQsL5uCGED2kH4LeETSryPi/8ri6AeMiIiZkoan/cGAgCmSDoiIe5q5lgnA6Ih4TNKewG+Bg9KxbYB9ImJVSiTy+yNzfVwM/Coi7pX0MbKEZufye1B+YkmjgFEA3TbZopkwzcysKCcOXUxEvCbpOmAl2bvoY1L5XZI2l7RJqjql7IF5ENlowfCIeCWV3QdMlPQ/wI25undGxAoASYuB7YDyxOGJiJiZtoenr3lpvydZIlExcZDUE9iHbOqlVNw9V2VyRKyqsl8yDOif62OT1Dd88B68JyImkCUudO/TLyrFaWZmLePEoWt6N31V81rZ/uNkw/Y7Ag0AETE6vdM/HJgjaVCq+1au3Sqa/jnI9y/g/Ii4rFj4QLbw9uWIGFAw/vL9fD97RcSb+cKUSFRqY2ZmHcS/VdG1zQBOBJA0BHg+N5pQ7gmy0YmrJX0qtdkhIh6MiHOB54BtWxnHbcCppXf6kvpK2rJagxTnUknHpTaStFsrzj0VOK20I2lAK/owM7N24sShaxsLDEqLBccBI6pVjoglZInG5LQw8QJJjZIeAu4HFrQmiIiYCvwReEBSI3A9sHGBpicCX5G0AFgEHNWK058O1EtamKZVRreiDzMzayeK8PSvrd3q6+ujoaGh1mGYma1RJM2JiPryco84mJmZWWFOHMzMzKwwJw5mZmZWmBMHMzMzK8yJg5mZmRXm36qwtZ6kV4FHah1HAb2B52sdREFrSqyOs/2tKbE6zrbbLiI+8Jn9/uRI+zB4pKlfKepqJDWsCXHCmhOr42x/a0qsjrPjeKrCzMzMCnPiYGZmZoU5cbAPgwm1DqCgNSVOWHNidZztb02J1XF2EC+ONDMzs8I84mBmZmaFOXEwMzOzwpw42FpL0iGSHpH0d0ljahzLtpKmSVosaZGkb6XysZKWS5qfvg7Ltfl+iv0RSQd3crzL0p9kny+pIZVtJul2SY+l75umckm6JMW6UNLATorxk7n7Nl/SK5LO6Cr3VNIVkp5Nf9a+VNbieyhpRKr/mKQRnRTnBZKWpFj+LOkjqbxO0hu5ezs+12ZQ+pn5e7oWdUKcLX6tO+P/hQqxXpeLc5mk+am8Zve01SLCX/5a676AbsDjwMeB9YEFQP8axtMHGJi2NwYeBfoDY4Ezm6jfP8XcHdg+XUu3Tox3GdC7rOznwJi0PQb4Wdo+DPhfQMBewIM1er3/BWzXVe4pcAAwEHiotfcQ2Az4R/q+adretBPiHA6sm7Z/louzLl+vrJ9ZKXalazm0E+Js0WvdWf8vNBVr2fFfAOfW+p629ssjDra2Ggz8PSL+ERH/BiYBR9UqmIh4OiLmpu1XgYeBvlWaHAVMioi3ImIp8Heya6qlo4Cr0vZVwOdz5VdHZibwEUl9Ojm2zwCPR8QTVep06j2NiHuAF5uIoSX38GDg9oh4MSJeAm4HDunoOCNiakS8k3ZnAttU6yPFuklEzIzsiXc1719bh8VZRaXXulP+X6gWaxo1+CLwp2p9dMY9bS0nDra26gv8X27/Sao/qDuNpDpgd+DBVPTNNCR8RWnomtrHH8BUSXMkjUplW0XE02n7X8BWabvWsQIcz+r/EXfFewotv4ddIeZTyd7tlmwvaZ6kuyXtn8r6pthKOjPOlrzWXeF+7g88ExGP5cq62j2tyomDWSeS1BO4ATgjIl4BfgfsAAwAniYbwuwK9ouIgcChwDckHZA/mN4BdYnf5Za0PnAkMDkVddV7upqudA8rkXQ28A5wbSp6GvhYROwOfAf4o6RNahUfa8hrXeYEVk9yu9o9bZYTB1tbLQe2ze1vk8pqRtJ6ZEnDtRFxI0BEPBMRqyLiXeD3vD90XtP4I2J5+v4s8OcU1zOlKYj0/dmuECtZcjM3Ip6BrntPk5bew5rFLGkkcARwYkpySEP/L6TtOWTrBXZMMeWnMzolzla81jX9GZC0LvAF4LpSWVe7p0U4cbC11Wygn6Tt0zvS44EptQomzWv+N/BwRPwyV55fC3A0UFqFPQU4XlJ3SdsD/cgWSnVGrBtJ2ri0TbZQ7qEUU2lV/wjgL7lYT06/GbAXsCI3HN8ZVnsH1xXvaU5L7+FtwHBJm6Zh+OGprENJOgT4LnBkRLyeK99CUre0/XGye/iPFOsrkvZKP+sn566tI+Ns6Wtd6/8XhgFLIuK9KYiudk8LqfXqTH/5q6O+yFaqP0qWwZ9d41j2IxuWXgjMT1+HAdcAjal8CtAn1+bsFPsjdOJqarIV5wvS16LSvQM2B+4EHgPuADZL5QJ+k2JtBOo7MdaNgBeAXrmyLnFPyZKZp4G3yeanv9Kae0i2xuDv6euUTorz72RrAUo/q+NT3WPSz8R8YC7wuVw/9WQP7seBS0mfTNzBcbb4te6M/xeaijWVTwRGl9Wt2T1t7Zc/ctrMzMwK81SFmZmZFebEwczMzApz4mBmZmaFOXEwMzOzwpw4mJmZWWFOHMzMzKwwJw5mZmZW2P8HTVSW59uscR8AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['Primary Breed'].value_counts().head(10).plot(kind='barh')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What are the most popular dog names?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "UNKNOWN     203\n",
       "Max         202\n",
       "Bella       193\n",
       "Charlie     172\n",
       "Lola        146\n",
       "Rocky       140\n",
       "Lucy        128\n",
       "Coco        114\n",
       "Buddy       113\n",
       "Lucky       106\n",
       "Daisy        90\n",
       "Lily         88\n",
       "Princess     86\n",
       "Bailey       83\n",
       "Luna         81\n",
       "Molly        81\n",
       "Toby         79\n",
       "Oliver       79\n",
       "Chloe        78\n",
       "Teddy        76\n",
       "Name: Animal Name, dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Animal Name'].value_counts().head(20)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Do any dogs have your name? How many dogs are named \"Max,\" and how many are named \"Maxwell\"?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "24"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#df.columns = [c.lower().replace(' ', '_') for c in df.columns]\n",
    "df[df.animal_name == 'Mimi'].animal_name.count()\n",
    "# There are a couple of Mimis :)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "202"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.animal_name == 'Max'].animal_name.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.animal_name == 'Maxwell'].animal_name.count()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What percentage of dogs are guard dogs?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No     99.914254\n",
       "Yes     0.085746\n",
       "Name: guard_or_trained, dtype: float64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.guard_or_trained.value_counts(normalize = True) * 100"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What are the actual numbers?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No     19809\n",
       "Yes       17\n",
       "Name: guard_or_trained, dtype: int64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.guard_or_trained.value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Wait... if you add that up, is it the same as your number of rows? Where are the other dogs???? How can we find them??????\n",
    "\n",
    "Use your `.head()` to think about it, then you'll do some magic with `.value_counts()`. Think about missing data!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No     19809\n",
       "NaN    10174\n",
       "Yes       17\n",
       "Name: guard_or_trained, dtype: int64"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.guard_or_trained.value_counts(dropna = False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Maybe fill in all of those empty \"Guard or Trained\" columns with \"No\"? Or as `NaN`? \n",
    "\n",
    "Can we make an assumption either way? Then check your result with another `.value_counts()`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "No     29983\n",
       "Yes       17\n",
       "Name: guard_or_trained, dtype: int64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.guard_or_trained.fillna('No').value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What are the top dog breeds for guard dogs? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "German Shepherd Dog           3\n",
       "Poodle, Standard              1\n",
       "German Shepherd Crossbreed    1\n",
       "Labrador Retriever            1\n",
       "Doberman Pinscher             1\n",
       "Name: primary_breed, dtype: int64"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "guard_dogs = df[df.guard_or_trained == 'Yes']\n",
    "guard_dogs.primary_breed.value_counts().head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Create a new column called \"year\" that is the dog's year of birth\n",
    "\n",
    "The `Animal Birth` column is a datetime, so you can get the year out of it with the code `df['Animal Birth'].apply(lambda birth: birth.year)`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>owner_zip_code</th>\n",
       "      <th>animal_name</th>\n",
       "      <th>animal_gender</th>\n",
       "      <th>primary_breed</th>\n",
       "      <th>secondary_breed</th>\n",
       "      <th>animal_dominant_color</th>\n",
       "      <th>animal_secondary_color</th>\n",
       "      <th>animal_third_color</th>\n",
       "      <th>animal_birth</th>\n",
       "      <th>spayed_or_neut</th>\n",
       "      <th>guard_or_trained</th>\n",
       "      <th>vaccinated</th>\n",
       "      <th>application_date</th>\n",
       "      <th>license_issued_date</th>\n",
       "      <th>license_expired_date</th>\n",
       "      <th>year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10024</td>\n",
       "      <td>BLUE MACK</td>\n",
       "      <td>M</td>\n",
       "      <td>NaN</td>\n",
       "      <td>AIREDALE TERR</td>\n",
       "      <td>BROWN</td>\n",
       "      <td>BLACK</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2007-11-01</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>2012-09-19 16:01:19.647</td>\n",
       "      <td>2015-09-19</td>\n",
       "      <td>2016-09-19</td>\n",
       "      <td>2007</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10461</td>\n",
       "      <td>Indie Zephir</td>\n",
       "      <td>M</td>\n",
       "      <td>Rottweiler</td>\n",
       "      <td>NaN</td>\n",
       "      <td>BLACK</td>\n",
       "      <td>TAN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2013-04-01</td>\n",
       "      <td>No</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>2013-09-20 11:41:36.647</td>\n",
       "      <td>2014-09-20</td>\n",
       "      <td>2018-09-20</td>\n",
       "      <td>2013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10013</td>\n",
       "      <td>Bilal</td>\n",
       "      <td>M</td>\n",
       "      <td>Australian Cattledog</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Rust</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2014-09-01</td>\n",
       "      <td>Yes</td>\n",
       "      <td>NaN</td>\n",
       "      <td>No</td>\n",
       "      <td>2014-09-12 13:13:36.713</td>\n",
       "      <td>2014-09-12</td>\n",
       "      <td>2019-09-12</td>\n",
       "      <td>2014</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>10025</td>\n",
       "      <td>Buddy</td>\n",
       "      <td>M</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Cockapoo</td>\n",
       "      <td>BLOND</td>\n",
       "      <td>WHITE</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2008-04-01</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>2014-09-12 15:26:51.417</td>\n",
       "      <td>2014-09-12</td>\n",
       "      <td>2017-10-20</td>\n",
       "      <td>2008</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>10013</td>\n",
       "      <td>Ali</td>\n",
       "      <td>M</td>\n",
       "      <td>Basenji</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Black</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2014-01-01</td>\n",
       "      <td>No</td>\n",
       "      <td>NaN</td>\n",
       "      <td>No</td>\n",
       "      <td>2014-09-12 15:43:17.707</td>\n",
       "      <td>2014-09-12</td>\n",
       "      <td>2019-09-12</td>\n",
       "      <td>2014</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   owner_zip_code   animal_name animal_gender         primary_breed  \\\n",
       "0           10024     BLUE MACK             M                   NaN   \n",
       "1           10461  Indie Zephir             M            Rottweiler   \n",
       "2           10013         Bilal             M  Australian Cattledog   \n",
       "3           10025         Buddy             M                   NaN   \n",
       "4           10013           Ali             M               Basenji   \n",
       "\n",
       "  secondary_breed animal_dominant_color animal_secondary_color  \\\n",
       "0   AIREDALE TERR                 BROWN                  BLACK   \n",
       "1             NaN                 BLACK                    TAN   \n",
       "2             NaN                  Rust                    NaN   \n",
       "3        Cockapoo                 BLOND                  WHITE   \n",
       "4             NaN                 Black                    NaN   \n",
       "\n",
       "  animal_third_color animal_birth spayed_or_neut guard_or_trained vaccinated  \\\n",
       "0                NaN   2007-11-01            Yes               No        Yes   \n",
       "1                NaN   2013-04-01             No               No        Yes   \n",
       "2                NaN   2014-09-01            Yes              NaN         No   \n",
       "3                NaN   2008-04-01            Yes               No        Yes   \n",
       "4                NaN   2014-01-01             No              NaN         No   \n",
       "\n",
       "         application_date license_issued_date license_expired_date  year  \n",
       "0 2012-09-19 16:01:19.647          2015-09-19           2016-09-19  2007  \n",
       "1 2013-09-20 11:41:36.647          2014-09-20           2018-09-20  2013  \n",
       "2 2014-09-12 13:13:36.713          2014-09-12           2019-09-12  2014  \n",
       "3 2014-09-12 15:26:51.417          2014-09-12           2017-10-20  2008  \n",
       "4 2014-09-12 15:43:17.707          2014-09-12           2019-09-12  2014  "
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['year'] = df['animal_birth'].apply(lambda birth: birth.year)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Calculate a new column called “age” that shows approximately how old the dog is. How old are dogs on average?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12.0"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['age'] = 2022 - df['year']\n",
    "df.age.median()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Joining data together"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Which neighborhood does each dog live in?\n",
    "\n",
    "You also have a (terrible) list of NYC neighborhoods in `zipcodes-neighborhoods.csv`. Join these two datasets together, so we know what neighborhood each dog lives in. **Be sure to not read it in as `df`, or else you'll overwrite your dogs dataframe.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>neighborhood</th>\n",
       "      <th>zip</th>\n",
       "      <th>borough</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Central Bronx</td>\n",
       "      <td>10453</td>\n",
       "      <td>Bronx</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Central Bronx</td>\n",
       "      <td>10457</td>\n",
       "      <td>Bronx</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Central Bronx</td>\n",
       "      <td>10460</td>\n",
       "      <td>Bronx</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Bronx Park and Fordham</td>\n",
       "      <td>10458</td>\n",
       "      <td>Bronx</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Bronx Park and Fordham</td>\n",
       "      <td>10467</td>\n",
       "      <td>Bronx</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>173</th>\n",
       "      <td>South Shore</td>\n",
       "      <td>10312</td>\n",
       "      <td>Staten Island</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>174</th>\n",
       "      <td>Stapleton and St. George</td>\n",
       "      <td>10301</td>\n",
       "      <td>Staten Island</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>175</th>\n",
       "      <td>Stapleton and St. George</td>\n",
       "      <td>10304</td>\n",
       "      <td>Staten Island</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>176</th>\n",
       "      <td>Stapleton and St. George</td>\n",
       "      <td>10305</td>\n",
       "      <td>Staten Island</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>177</th>\n",
       "      <td>Mid-Island</td>\n",
       "      <td>10314</td>\n",
       "      <td>Staten Island</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>178 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                 neighborhood    zip        borough\n",
       "0               Central Bronx  10453          Bronx\n",
       "1               Central Bronx  10457          Bronx\n",
       "2               Central Bronx  10460          Bronx\n",
       "3      Bronx Park and Fordham  10458          Bronx\n",
       "4      Bronx Park and Fordham  10467          Bronx\n",
       "..                        ...    ...            ...\n",
       "173               South Shore  10312  Staten Island\n",
       "174  Stapleton and St. George  10301  Staten Island\n",
       "175  Stapleton and St. George  10304  Staten Island\n",
       "176  Stapleton and St. George  10305  Staten Island\n",
       "177                Mid-Island  10314  Staten Island\n",
       "\n",
       "[178 rows x 3 columns]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zip_df = pd.read_csv(\"zipcodes-neighborhoods.csv\")\n",
    "zip_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>owner_zip_code</th>\n",
       "      <th>animal_name</th>\n",
       "      <th>animal_gender</th>\n",
       "      <th>primary_breed</th>\n",
       "      <th>secondary_breed</th>\n",
       "      <th>animal_dominant_color</th>\n",
       "      <th>animal_secondary_color</th>\n",
       "      <th>animal_third_color</th>\n",
       "      <th>animal_birth</th>\n",
       "      <th>spayed_or_neut</th>\n",
       "      <th>guard_or_trained</th>\n",
       "      <th>vaccinated</th>\n",
       "      <th>application_date</th>\n",
       "      <th>license_issued_date</th>\n",
       "      <th>license_expired_date</th>\n",
       "      <th>year</th>\n",
       "      <th>age</th>\n",
       "      <th>neighborhood</th>\n",
       "      <th>zip</th>\n",
       "      <th>borough</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10024</td>\n",
       "      <td>BLUE MACK</td>\n",
       "      <td>M</td>\n",
       "      <td>NaN</td>\n",
       "      <td>AIREDALE TERR</td>\n",
       "      <td>BROWN</td>\n",
       "      <td>BLACK</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2007-11-01</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>2012-09-19 16:01:19.647</td>\n",
       "      <td>2015-09-19</td>\n",
       "      <td>2016-09-19</td>\n",
       "      <td>2007</td>\n",
       "      <td>15</td>\n",
       "      <td>Upper West Side</td>\n",
       "      <td>10024</td>\n",
       "      <td>Manhattan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10024</td>\n",
       "      <td>Louie</td>\n",
       "      <td>M</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Coonhound</td>\n",
       "      <td>Black</td>\n",
       "      <td>White</td>\n",
       "      <td>Brown</td>\n",
       "      <td>2008-05-01</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>2014-09-15 16:36:20.200</td>\n",
       "      <td>2014-09-15</td>\n",
       "      <td>2017-09-03</td>\n",
       "      <td>2008</td>\n",
       "      <td>14</td>\n",
       "      <td>Upper West Side</td>\n",
       "      <td>10024</td>\n",
       "      <td>Manhattan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10024</td>\n",
       "      <td>Tosha</td>\n",
       "      <td>F</td>\n",
       "      <td>Collie, Smooth Coat</td>\n",
       "      <td>NaN</td>\n",
       "      <td>BLUE MERLE</td>\n",
       "      <td>WHITE</td>\n",
       "      <td>TAN</td>\n",
       "      <td>2011-12-01</td>\n",
       "      <td>Yes</td>\n",
       "      <td>No</td>\n",
       "      <td>Yes</td>\n",
       "      <td>2014-09-16 10:22:07.867</td>\n",
       "      <td>2014-09-16</td>\n",
       "      <td>2017-10-11</td>\n",
       "      <td>2011</td>\n",
       "      <td>11</td>\n",
       "      <td>Upper West Side</td>\n",
       "      <td>10024</td>\n",
       "      <td>Manhattan</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   owner_zip_code animal_name animal_gender        primary_breed  \\\n",
       "0           10024   BLUE MACK             M                  NaN   \n",
       "1           10024       Louie             M                  NaN   \n",
       "2           10024       Tosha             F  Collie, Smooth Coat   \n",
       "\n",
       "  secondary_breed animal_dominant_color animal_secondary_color  \\\n",
       "0   AIREDALE TERR                 BROWN                  BLACK   \n",
       "1       Coonhound                 Black                  White   \n",
       "2             NaN            BLUE MERLE                  WHITE   \n",
       "\n",
       "  animal_third_color animal_birth spayed_or_neut guard_or_trained vaccinated  \\\n",
       "0                NaN   2007-11-01            Yes               No        Yes   \n",
       "1              Brown   2008-05-01            Yes               No        Yes   \n",
       "2                TAN   2011-12-01            Yes               No        Yes   \n",
       "\n",
       "         application_date license_issued_date license_expired_date  year  age  \\\n",
       "0 2012-09-19 16:01:19.647          2015-09-19           2016-09-19  2007   15   \n",
       "1 2014-09-15 16:36:20.200          2014-09-15           2017-09-03  2008   14   \n",
       "2 2014-09-16 10:22:07.867          2014-09-16           2017-10-11  2011   11   \n",
       "\n",
       "      neighborhood    zip    borough  \n",
       "0  Upper West Side  10024  Manhattan  \n",
       "1  Upper West Side  10024  Manhattan  \n",
       "2  Upper West Side  10024  Manhattan  "
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merged = df.merge(zip_df, left_on='owner_zip_code', right_on='zip')\n",
    "merged.head(3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What is the most popular dog name in all parts of the Bronx? How about Brooklyn? The Upper East Side?\n",
    "\n",
    "You'll want to do these separately, and filter for each."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Bella       22\n",
       "Max         21\n",
       "Rocky       20\n",
       "Princess    15\n",
       "Lucky       15\n",
       "Name: animal_name, dtype: int64"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merged[merged.borough == 'Bronx'].animal_name.value_counts().head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Max        46\n",
       "unknown    45\n",
       "UNKNOWN    45\n",
       "Bella      45\n",
       "Charlie    42\n",
       "Name: animal_name, dtype: int64"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merged[merged.borough == 'Brooklyn'].animal_name.value_counts().head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Charlie    19\n",
       "Bella      12\n",
       "NO NAME    11\n",
       "Lola       10\n",
       "Lucy       10\n",
       "Name: animal_name, dtype: int64"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merged[merged.neighborhood == 'Upper East Side'].animal_name.value_counts().head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What is the most common dog breed in each of the neighborhoods of NYC?\n",
    "\n",
    "* *Tip: There are a few ways to do this, and some are awful (see the \"top 5 breeds in each borough\" question below).*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "neighborhood  primary_breed              \n",
       "Borough Park  Yorkshire Terrier              49\n",
       "              Maltese                        34\n",
       "              Shih Tzu                       34\n",
       "              Chihuahua                      32\n",
       "              Labrador Retriever             19\n",
       "                                             ..\n",
       "West Queens   Soft Coated Wheaten Terrier     1\n",
       "              Tibetan Spaniel                 1\n",
       "              Toy Fox Terrier                 1\n",
       "              Weimaraner                      1\n",
       "              Wire Fox Terrier                1\n",
       "Name: primary_breed, Length: 3987, dtype: int64"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merged.groupby(by = 'neighborhood').primary_breed.value_counts()\n",
    "# ??"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What breed of dogs are the least likely to be spayed? Male or female?\n",
    "\n",
    "* *Tip: This has a handful of interpretations, and some are easier than others. Feel free to skip it if you can't figure it out to your satisfaction.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Yorkshire Terrier                     531\n",
       "Shih Tzu                              401\n",
       "Chihuahua                             303\n",
       "Maltese                               300\n",
       "American Pit Bull Terrier/Pit Bull    173\n",
       "Name: primary_breed, dtype: int64"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merged.query(\"spayed_or_neut == 'No'\").primary_breed.value_counts().head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "animal_gender  spayed_or_neut\n",
       "               Yes                   3\n",
       "F              Yes               11620\n",
       "               No                 1930\n",
       "M              Yes               12677\n",
       "               No                 3343\n",
       "Name: spayed_or_neut, dtype: int64"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merged.groupby(by='animal_gender').spayed_or_neut.value_counts(sort=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# ???"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Make a new column called `monochrome` that is True for any animal that only has black, white or grey as one of its colors. How many animals are monochrome?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "BLACK    5250\n",
       "WHITE    4228\n",
       "Black    2844\n",
       "White    2376\n",
       "BROWN    2018\n",
       "Name: animal_dominant_color, dtype: int64"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 1. Explore the results Animal Dominant Color\n",
    "merged.animal_dominant_color.value_counts().head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>owner_zip_code</th>\n",
       "      <th>animal_name</th>\n",
       "      <th>animal_gender</th>\n",
       "      <th>primary_breed</th>\n",
       "      <th>secondary_breed</th>\n",
       "      <th>animal_dominant_color</th>\n",
       "      <th>animal_secondary_color</th>\n",
       "      <th>animal_third_color</th>\n",
       "      <th>animal_birth</th>\n",
       "      <th>spayed_or_neut</th>\n",
       "      <th>guard_or_trained</th>\n",
       "      <th>vaccinated</th>\n",
       "      <th>application_date</th>\n",
       "      <th>license_issued_date</th>\n",
       "      <th>license_expired_date</th>\n",
       "      <th>year</th>\n",
       "      <th>age</th>\n",
       "      <th>neighborhood</th>\n",
       "      <th>zip</th>\n",
       "      <th>borough</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [owner_zip_code, animal_name, animal_gender, primary_breed, secondary_breed, animal_dominant_color, animal_secondary_color, animal_third_color, animal_birth, spayed_or_neut, guard_or_trained, vaccinated, application_date, license_issued_date, license_expired_date, year, age, neighborhood, zip, borough]\n",
       "Index: []"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 2. Filter\n",
    "merged[merged.animal_dominant_color.str.contains(\"black\", na=False)]\n",
    "\n",
    "# 2. Create the column \n",
    "# merged['monochrome'] = \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## How many dogs are in each borough? Plot it in a graph."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "merged.borough.value_counts().plot.bar()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Which borough has the highest number of dogs per-capita?\n",
    "\n",
    "You’ll need to merge in `population_boro.csv`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Make a bar graph of the top 5 breeds in each borough.\n",
    "\n",
    "How do you groupby and then only take the top X number? You **really** should ask me, because it's kind of crazy."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

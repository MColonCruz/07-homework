{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "# Homework 7, Part One: Lots and lots of questions about beer"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Do your importing and your setup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 487,
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
    "## Read in the file `craftcans.csv`, and look at the first first rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 488,
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
       "      <th>Beer</th>\n",
       "      <th>Brewery</th>\n",
       "      <th>Location</th>\n",
       "      <th>Style</th>\n",
       "      <th>Size</th>\n",
       "      <th>ABV</th>\n",
       "      <th>IBUs</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Get Together</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.50%</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Maggie's Leap</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>Milk / Sweet Stout</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.90%</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Wall's End</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>English Brown Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.80%</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Pumpion</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>Pumpkin Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.00%</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Stronghold</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>American Porter</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.00%</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2411</th>\n",
       "      <td>Mama's Little Yella Pils</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>Czech Pilsener</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>5.30%</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2412</th>\n",
       "      <td>GUBNA Imperial IPA</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>9.90%</td>\n",
       "      <td>100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2413</th>\n",
       "      <td>Old Chub</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>Scottish Ale</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>8.00%</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2414</th>\n",
       "      <td>Gordon Ale (2009)</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>8.70%</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2415</th>\n",
       "      <td>Dale's Pale Ale</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>American Pale Ale (APA)</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>6.50%</td>\n",
       "      <td>65</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2416 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                          Beer              Brewery         Location  \\\n",
       "0                 Get Together    NorthGate Brewing  Minneapolis, MN   \n",
       "1                Maggie's Leap    NorthGate Brewing  Minneapolis, MN   \n",
       "2                   Wall's End    NorthGate Brewing  Minneapolis, MN   \n",
       "3                      Pumpion    NorthGate Brewing  Minneapolis, MN   \n",
       "4                   Stronghold    NorthGate Brewing  Minneapolis, MN   \n",
       "...                        ...                  ...              ...   \n",
       "2411  Mama's Little Yella Pils  Oskar Blues Brewery     Longmont, CO   \n",
       "2412        GUBNA Imperial IPA  Oskar Blues Brewery     Longmont, CO   \n",
       "2413                  Old Chub  Oskar Blues Brewery     Longmont, CO   \n",
       "2414         Gordon Ale (2009)  Oskar Blues Brewery     Longmont, CO   \n",
       "2415           Dale's Pale Ale  Oskar Blues Brewery     Longmont, CO   \n",
       "\n",
       "                               Style    Size    ABV IBUs  \n",
       "0                       American IPA  16 oz.  4.50%   50  \n",
       "1                 Milk / Sweet Stout  16 oz.  4.90%   26  \n",
       "2                  English Brown Ale  16 oz.  4.80%   19  \n",
       "3                        Pumpkin Ale  16 oz.  6.00%   38  \n",
       "4                    American Porter  16 oz.  6.00%   25  \n",
       "...                              ...     ...    ...  ...  \n",
       "2411                  Czech Pilsener  12 oz.  5.30%   35  \n",
       "2412  American Double / Imperial IPA  12 oz.  9.90%  100  \n",
       "2413                    Scottish Ale  12 oz.  8.00%   35  \n",
       "2414  American Double / Imperial IPA  12 oz.  8.70%   85  \n",
       "2415         American Pale Ale (APA)  12 oz.  6.50%   65  \n",
       "\n",
       "[2416 rows x 7 columns]"
      ]
     },
     "execution_count": 488,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv('craftcans.csv')\n",
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## How many rows do you have in the data? What are the column types?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 489,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2416, 7)"
      ]
     },
     "execution_count": 489,
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
   "execution_count": 490,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Beer        object\n",
       "Brewery     object\n",
       "Location    object\n",
       "Style       object\n",
       "Size        object\n",
       "ABV         object\n",
       "IBUs        object\n",
       "dtype: object"
      ]
     },
     "execution_count": 490,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Checking out our alcohol"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What are the top 10 producers of cans of beer?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 491,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Brewery Vivant                62\n",
       "Oskar Blues Brewery           46\n",
       "Sun King Brewing Company      38\n",
       "Cigar City Brewing Company    25\n",
       "Sixpoint Craft Ales           24\n",
       "Hopworks Urban Brewery        23\n",
       "Stevens Point Brewery         22\n",
       "Great Crescent Brewery        20\n",
       "21st Amendment Brewery        20\n",
       "Bonfire Brewing Company       19\n",
       "Name: Brewery, dtype: int64"
      ]
     },
     "execution_count": 491,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Brewery.value_counts().head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What is the most common ABV? (alcohol by volume)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 492,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    5.00%\n",
       "Name: ABV, dtype: object"
      ]
     },
     "execution_count": 492,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.ABV.mode()\n",
    "# Also: df.ABV.value_counts().head(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Oh, weird, ABV isn't a number. Convert it to a number for me, please.\n",
    "\n",
    "It's going to take a few steps!\n",
    "\n",
    "### First, let's just look at the ABV column by itself"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 493,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       4.50%\n",
       "1       4.90%\n",
       "2       4.80%\n",
       "3       6.00%\n",
       "4       6.00%\n",
       "        ...  \n",
       "2411    5.30%\n",
       "2412    9.90%\n",
       "2413    8.00%\n",
       "2414    8.70%\n",
       "2415    6.50%\n",
       "Name: ABV, Length: 2416, dtype: object"
      ]
     },
     "execution_count": 493,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.ABV"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Hm, `%` isn't part of  a number. Let's remove it.\n",
    "\n",
    "When you're confident you got it right, save the results back into the `ABV` column.\n",
    "\n",
    "- *Tip: In programming the easiest way to remove something is to *replacing it with nothing*.\n",
    "- *Tip: \"nothing\" might seem like `NaN` sinc we talked about it a lot in class, but in this case it isn't! It's just an empty string, like \"\"*\n",
    "- *Tip: `.replace` is usually used for replacing ENTIRE cells, while `.str.replace` is useful for replacing PARTS of cells*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 494,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       4.50 \n",
       "1       4.90 \n",
       "2       4.80 \n",
       "3       6.00 \n",
       "4       6.00 \n",
       "        ...  \n",
       "2411    5.30 \n",
       "2412    9.90 \n",
       "2413    8.00 \n",
       "2414    8.70 \n",
       "2415    6.50 \n",
       "Name: ABV, Length: 2416, dtype: object"
      ]
     },
     "execution_count": 494,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.ABV = df.ABV.str.replace(\"%\", \" \")\n",
    "df.ABV"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Now let's turn `ABV` into a numeric data type\n",
    "\n",
    "Save the results back into the `ABV` column (again), and then check `df.dtypes` to make sure it worked.\n",
    "\n",
    "- *Tip: We used `.astype(int)` during class, but this has a decimal in it...*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 495,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       4.5\n",
       "1       4.9\n",
       "2       4.8\n",
       "3       6.0\n",
       "4       6.0\n",
       "       ... \n",
       "2411    5.3\n",
       "2412    9.9\n",
       "2413    8.0\n",
       "2414    8.7\n",
       "2415    6.5\n",
       "Name: ABV, Length: 2416, dtype: float64"
      ]
     },
     "execution_count": 495,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.ABV = df.ABV.astype(float)\n",
    "df.ABV"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What's the ABV of the average beer look like?\n",
    "\n",
    "### Show me in two different ways: one command to show the `median`/`mean`/etc, and secondly show me a chart"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 496,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    2348.000000\n",
       "mean        5.977342\n",
       "std         1.354173\n",
       "min         0.100000\n",
       "25%         5.000000\n",
       "50%         5.600000\n",
       "75%         6.700000\n",
       "max        12.800000\n",
       "Name: ABV, dtype: float64"
      ]
     },
     "execution_count": 496,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.ABV.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 497,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 497,
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
    "df.ABV.hist()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### We don't have ABV for all of the beers, how many are we missing them from?\n",
    "\n",
    "- *Tip: You can use `isna()` or `notna()` to see where a column is missing/not missing data.*\n",
    "- *Tip: You just want to count how many `True`s and `False`s there are.*\n",
    "- *Tip: It's a weird trick involving something we usually use to count things in a column*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 498,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False    2348\n",
       "True       68\n",
       "Name: ABV, dtype: int64"
      ]
     },
     "execution_count": 498,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.ABV.isna().value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Looking at location\n",
    "\n",
    "Brooklyn used to produce 80% of the country's beer! Let's see if it's still true."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What are the top 10 cities in the US for canned craft beer?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 499,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Grand Rapids, MI    66\n",
       "Chicago, IL         55\n",
       "Portland, OR        52\n",
       "Indianapolis, IN    43\n",
       "San Diego, CA       42\n",
       "Boulder, CO         41\n",
       "Denver, CO          40\n",
       "Brooklyn, NY        38\n",
       "Seattle, WA         35\n",
       "Longmont, CO        33\n",
       "Name: Location, dtype: int64"
      ]
     },
     "execution_count": 499,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Location.value_counts().head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## List all of the beer from Brooklyn, NY"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 500,
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
       "      <th>Beer</th>\n",
       "      <th>Brewery</th>\n",
       "      <th>Location</th>\n",
       "      <th>Style</th>\n",
       "      <th>Size</th>\n",
       "      <th>ABV</th>\n",
       "      <th>IBUs</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>115</th>\n",
       "      <td>4Beans</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Baltic Porter</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>10.0</td>\n",
       "      <td>52</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>210</th>\n",
       "      <td>Jammer</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Gose</td>\n",
       "      <td>12 oz. Slimline</td>\n",
       "      <td>4.2</td>\n",
       "      <td>16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>246</th>\n",
       "      <td>Abigale</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Belgian Pale Ale</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>8.0</td>\n",
       "      <td>Does not apply</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>404</th>\n",
       "      <td>Nomader Weiss</td>\n",
       "      <td>Evil Twin Brewing</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Berliner Weissbier</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>4.0</td>\n",
       "      <td>Does not apply</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>421</th>\n",
       "      <td>Rad</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Fruit / Vegetable Beer</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>3.2</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>439</th>\n",
       "      <td>Molotov Lite</td>\n",
       "      <td>Evil Twin Brewing</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>8.5</td>\n",
       "      <td>Does not apply</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>588</th>\n",
       "      <td>Bengali</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>24 oz. \"Silo Can\"</td>\n",
       "      <td>6.5</td>\n",
       "      <td>62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>713</th>\n",
       "      <td>Sensi Harvest</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Pale Ale (APA)</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>4.7</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>969</th>\n",
       "      <td>Hi-Res</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>9.9</td>\n",
       "      <td>111</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>987</th>\n",
       "      <td>KelSo Nut Brown Lager</td>\n",
       "      <td>KelSo Beer Company</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Euro Dark Lager</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>5.7</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1057</th>\n",
       "      <td>Global Warmer</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Strong Ale</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>7.0</td>\n",
       "      <td>70</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1074</th>\n",
       "      <td>Autumnation (2013)</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.7</td>\n",
       "      <td>74</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1093</th>\n",
       "      <td>KelSo India Pale Ale</td>\n",
       "      <td>KelSo Beer Company</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>6.0</td>\n",
       "      <td>64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1267</th>\n",
       "      <td>The Crisp</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>German Pilsener</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.4</td>\n",
       "      <td>42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1268</th>\n",
       "      <td>Sweet Action</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Cream Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.2</td>\n",
       "      <td>34</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1269</th>\n",
       "      <td>Righteous Ale</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Rye Beer</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.3</td>\n",
       "      <td>57</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1270</th>\n",
       "      <td>Bengali Tiger</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.4</td>\n",
       "      <td>62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1305</th>\n",
       "      <td>KelSo Pilsner</td>\n",
       "      <td>KelSo Beer Company</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Czech Pilsener</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>5.5</td>\n",
       "      <td>23</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1365</th>\n",
       "      <td>Hipster Ale (Two Roads Brewing)</td>\n",
       "      <td>Evil Twin Brewing</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Pale Ale (APA)</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>5.5</td>\n",
       "      <td>Does not apply</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1366</th>\n",
       "      <td>Bikini Beer</td>\n",
       "      <td>Evil Twin Brewing</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>2.7</td>\n",
       "      <td>Does not apply</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1373</th>\n",
       "      <td>East India Pale Ale</td>\n",
       "      <td>Brooklyn Brewery</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>English India Pale Ale (IPA)</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.8</td>\n",
       "      <td>47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1624</th>\n",
       "      <td>3Beans</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Baltic Porter</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>9.9</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1836</th>\n",
       "      <td>Brownstone</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Brown Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.9</td>\n",
       "      <td>47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1857</th>\n",
       "      <td>Brooklyn Summer Ale</td>\n",
       "      <td>Brooklyn Brewery</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>English Pale Mild Ale</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>4.5</td>\n",
       "      <td>Does not apply</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1962</th>\n",
       "      <td>Hipster Ale (Westbrook Brewing)</td>\n",
       "      <td>Evil Twin Brewing</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Pale Ale (APA)</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>5.5</td>\n",
       "      <td>Does not apply</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1970</th>\n",
       "      <td>Apollo</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Pale Wheat Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.2</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1971</th>\n",
       "      <td>Harbinger</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Saison / Farmhouse Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.9</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1972</th>\n",
       "      <td>Resin</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>9.1</td>\n",
       "      <td>103</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2027</th>\n",
       "      <td>East India Pale Ale</td>\n",
       "      <td>Brooklyn Brewery</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>English India Pale Ale (IPA)</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>6.8</td>\n",
       "      <td>47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2062</th>\n",
       "      <td>Diesel</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Stout</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.3</td>\n",
       "      <td>69</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2074</th>\n",
       "      <td>Autumnation (2011-12) (2011)</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Pumpkin Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.0</td>\n",
       "      <td>48</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2140</th>\n",
       "      <td>The Crisp (2011)</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>German Pilsener</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.4</td>\n",
       "      <td>42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2141</th>\n",
       "      <td>Sweet Action (2011)</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Cream Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.2</td>\n",
       "      <td>34</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2142</th>\n",
       "      <td>Righteous Ale (2011)</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Rye Beer</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.3</td>\n",
       "      <td>57</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2143</th>\n",
       "      <td>Bengali Tiger (2011)</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.4</td>\n",
       "      <td>62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2219</th>\n",
       "      <td>Brooklyn Summer Ale (2011)</td>\n",
       "      <td>Brooklyn Brewery</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>English Pale Mild Ale</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>4.5</td>\n",
       "      <td>Does not apply</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2350</th>\n",
       "      <td>Brooklyn Lager (16 oz.)</td>\n",
       "      <td>Brooklyn Brewery</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Amber / Red Lager</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.2</td>\n",
       "      <td>Does not apply</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2351</th>\n",
       "      <td>Brooklyn Lager (12 oz.)</td>\n",
       "      <td>Brooklyn Brewery</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Amber / Red Lager</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>5.2</td>\n",
       "      <td>Does not apply</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                 Beer              Brewery      Location  \\\n",
       "115                            4Beans  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "210                            Jammer  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "246                           Abigale  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "404                     Nomader Weiss    Evil Twin Brewing  Brooklyn, NY   \n",
       "421                               Rad  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "439                      Molotov Lite    Evil Twin Brewing  Brooklyn, NY   \n",
       "588                           Bengali  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "713                     Sensi Harvest  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "969                            Hi-Res  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "987             KelSo Nut Brown Lager   KelSo Beer Company  Brooklyn, NY   \n",
       "1057                    Global Warmer  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1074               Autumnation (2013)  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1093             KelSo India Pale Ale   KelSo Beer Company  Brooklyn, NY   \n",
       "1267                        The Crisp  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1268                     Sweet Action  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1269                    Righteous Ale  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1270                    Bengali Tiger  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1305                    KelSo Pilsner   KelSo Beer Company  Brooklyn, NY   \n",
       "1365  Hipster Ale (Two Roads Brewing)    Evil Twin Brewing  Brooklyn, NY   \n",
       "1366                      Bikini Beer    Evil Twin Brewing  Brooklyn, NY   \n",
       "1373              East India Pale Ale     Brooklyn Brewery  Brooklyn, NY   \n",
       "1624                           3Beans  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1836                       Brownstone  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1857              Brooklyn Summer Ale     Brooklyn Brewery  Brooklyn, NY   \n",
       "1962  Hipster Ale (Westbrook Brewing)    Evil Twin Brewing  Brooklyn, NY   \n",
       "1970                           Apollo  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1971                        Harbinger  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "1972                            Resin  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "2027              East India Pale Ale     Brooklyn Brewery  Brooklyn, NY   \n",
       "2062                           Diesel  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "2074     Autumnation (2011-12) (2011)  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "2140                 The Crisp (2011)  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "2141              Sweet Action (2011)  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "2142             Righteous Ale (2011)  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "2143             Bengali Tiger (2011)  Sixpoint Craft Ales  Brooklyn, NY   \n",
       "2219       Brooklyn Summer Ale (2011)     Brooklyn Brewery  Brooklyn, NY   \n",
       "2350          Brooklyn Lager (16 oz.)     Brooklyn Brewery  Brooklyn, NY   \n",
       "2351          Brooklyn Lager (12 oz.)     Brooklyn Brewery  Brooklyn, NY   \n",
       "\n",
       "                               Style               Size   ABV            IBUs  \n",
       "115                    Baltic Porter             12 oz.  10.0              52  \n",
       "210                             Gose    12 oz. Slimline   4.2              16  \n",
       "246                 Belgian Pale Ale             12 oz.   8.0  Does not apply  \n",
       "404               Berliner Weissbier             12 oz.   4.0  Does not apply  \n",
       "421           Fruit / Vegetable Beer             16 oz.   3.2               7  \n",
       "439   American Double / Imperial IPA             16 oz.   8.5  Does not apply  \n",
       "588                     American IPA  24 oz. \"Silo Can\"   6.5              62  \n",
       "713          American Pale Ale (APA)             12 oz.   4.7              50  \n",
       "969   American Double / Imperial IPA             12 oz.   9.9             111  \n",
       "987                  Euro Dark Lager             12 oz.   5.7              19  \n",
       "1057             American Strong Ale             12 oz.   7.0              70  \n",
       "1074                    American IPA             16 oz.   6.7              74  \n",
       "1093                    American IPA             12 oz.   6.0              64  \n",
       "1267                 German Pilsener             16 oz.   5.4              42  \n",
       "1268                       Cream Ale             16 oz.   5.2              34  \n",
       "1269                        Rye Beer             16 oz.   6.3              57  \n",
       "1270                    American IPA             16 oz.   6.4              62  \n",
       "1305                  Czech Pilsener             12 oz.   5.5              23  \n",
       "1365         American Pale Ale (APA)             12 oz.   5.5  Does not apply  \n",
       "1366                    American IPA             12 oz.   2.7  Does not apply  \n",
       "1373    English India Pale Ale (IPA)             16 oz.   6.8              47  \n",
       "1624                   Baltic Porter             12 oz.   9.9              85  \n",
       "1836              American Brown Ale             16 oz.   5.9              47  \n",
       "1857           English Pale Mild Ale             12 oz.   4.5  Does not apply  \n",
       "1962         American Pale Ale (APA)             12 oz.   5.5  Does not apply  \n",
       "1970         American Pale Wheat Ale             16 oz.   5.2              11  \n",
       "1971          Saison / Farmhouse Ale             16 oz.   4.9              35  \n",
       "1972  American Double / Imperial IPA             12 oz.   9.1             103  \n",
       "2027    English India Pale Ale (IPA)             12 oz.   6.8              47  \n",
       "2062                  American Stout             16 oz.   6.3              69  \n",
       "2074                     Pumpkin Ale             16 oz.   6.0              48  \n",
       "2140                 German Pilsener             16 oz.   5.4              42  \n",
       "2141                       Cream Ale             16 oz.   5.2              34  \n",
       "2142                        Rye Beer             16 oz.   6.3              57  \n",
       "2143                    American IPA             16 oz.   6.4              62  \n",
       "2219           English Pale Mild Ale             12 oz.   4.5  Does not apply  \n",
       "2350      American Amber / Red Lager             16 oz.   5.2  Does not apply  \n",
       "2351      American Amber / Red Lager             12 oz.   5.2  Does not apply  "
      ]
     },
     "execution_count": 500,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query(\"Location == 'Brooklyn, NY'\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What brewery in Brooklyn puts out the most types of canned beer?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 501,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    Sixpoint Craft Ales\n",
       "Name: Brewery, dtype: object"
      ]
     },
     "execution_count": 501,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "brooklyn.Brewery.mode()\n",
    "# brooklyn.Brewery.value_counts().head(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What are the five styles of beer that Sixpoint produces the most cans of?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 502,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "American IPA                      4\n",
       "Baltic Porter                     2\n",
       "American Double / Imperial IPA    2\n",
       "German Pilsener                   2\n",
       "Cream Ale                         2\n",
       "Name: Style, dtype: int64"
      ]
     },
     "execution_count": 502,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "brooklyn.query(\"Brewery == 'Sixpoint Craft Ales'\").Style.value_counts().head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## List all of the breweries in New York state.\n",
    "\n",
    "- *Tip: We want to match **part** of the `Location` column, but not all of it.*\n",
    "- *Tip: Watch out for `NaN` values! You might be close, but you'll need to pass an extra parameter to make it work without an error.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 503,
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
       "      <th>Beer</th>\n",
       "      <th>Brewery</th>\n",
       "      <th>Location</th>\n",
       "      <th>Style</th>\n",
       "      <th>Size</th>\n",
       "      <th>ABV</th>\n",
       "      <th>IBUs</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>115</th>\n",
       "      <td>4Beans</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Baltic Porter</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>10.0</td>\n",
       "      <td>52</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>210</th>\n",
       "      <td>Jammer</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Gose</td>\n",
       "      <td>12 oz. Slimline</td>\n",
       "      <td>4.2</td>\n",
       "      <td>16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>246</th>\n",
       "      <td>Abigale</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Belgian Pale Ale</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>8.0</td>\n",
       "      <td>Does not apply</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>404</th>\n",
       "      <td>Nomader Weiss</td>\n",
       "      <td>Evil Twin Brewing</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Berliner Weissbier</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>4.0</td>\n",
       "      <td>Does not apply</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>421</th>\n",
       "      <td>Rad</td>\n",
       "      <td>Sixpoint Craft Ales</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>Fruit / Vegetable Beer</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>3.2</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2351</th>\n",
       "      <td>Brooklyn Lager (12 oz.)</td>\n",
       "      <td>Brooklyn Brewery</td>\n",
       "      <td>Brooklyn, NY</td>\n",
       "      <td>American Amber / Red Lager</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>5.2</td>\n",
       "      <td>Does not apply</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2364</th>\n",
       "      <td>Heinnieweisse Weissebier</td>\n",
       "      <td>Butternuts Beer and Ale</td>\n",
       "      <td>Garrattsville, NY</td>\n",
       "      <td>Hefeweizen</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>4.9</td>\n",
       "      <td>Does not apply</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2365</th>\n",
       "      <td>Snapperhead IPA</td>\n",
       "      <td>Butternuts Beer and Ale</td>\n",
       "      <td>Garrattsville, NY</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>6.8</td>\n",
       "      <td>Does not apply</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2366</th>\n",
       "      <td>Moo Thunder Stout</td>\n",
       "      <td>Butternuts Beer and Ale</td>\n",
       "      <td>Garrattsville, NY</td>\n",
       "      <td>Milk / Sweet Stout</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>4.9</td>\n",
       "      <td>Does not apply</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2367</th>\n",
       "      <td>Porkslap Pale Ale</td>\n",
       "      <td>Butternuts Beer and Ale</td>\n",
       "      <td>Garrattsville, NY</td>\n",
       "      <td>American Pale Ale (APA)</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>4.3</td>\n",
       "      <td>Does not apply</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>74 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                          Beer                  Brewery           Location  \\\n",
       "115                     4Beans      Sixpoint Craft Ales       Brooklyn, NY   \n",
       "210                     Jammer      Sixpoint Craft Ales       Brooklyn, NY   \n",
       "246                    Abigale      Sixpoint Craft Ales       Brooklyn, NY   \n",
       "404              Nomader Weiss        Evil Twin Brewing       Brooklyn, NY   \n",
       "421                        Rad      Sixpoint Craft Ales       Brooklyn, NY   \n",
       "...                        ...                      ...                ...   \n",
       "2351   Brooklyn Lager (12 oz.)         Brooklyn Brewery       Brooklyn, NY   \n",
       "2364  Heinnieweisse Weissebier  Butternuts Beer and Ale  Garrattsville, NY   \n",
       "2365           Snapperhead IPA  Butternuts Beer and Ale  Garrattsville, NY   \n",
       "2366         Moo Thunder Stout  Butternuts Beer and Ale  Garrattsville, NY   \n",
       "2367         Porkslap Pale Ale  Butternuts Beer and Ale  Garrattsville, NY   \n",
       "\n",
       "                           Style             Size   ABV            IBUs  \n",
       "115                Baltic Porter           12 oz.  10.0              52  \n",
       "210                         Gose  12 oz. Slimline   4.2              16  \n",
       "246             Belgian Pale Ale           12 oz.   8.0  Does not apply  \n",
       "404           Berliner Weissbier           12 oz.   4.0  Does not apply  \n",
       "421       Fruit / Vegetable Beer           16 oz.   3.2               7  \n",
       "...                          ...              ...   ...             ...  \n",
       "2351  American Amber / Red Lager           12 oz.   5.2  Does not apply  \n",
       "2364                  Hefeweizen           12 oz.   4.9  Does not apply  \n",
       "2365                American IPA           12 oz.   6.8  Does not apply  \n",
       "2366          Milk / Sweet Stout           12 oz.   4.9  Does not apply  \n",
       "2367     American Pale Ale (APA)           12 oz.   4.3  Does not apply  \n",
       "\n",
       "[74 rows x 7 columns]"
      ]
     },
     "execution_count": 503,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Is there a way of doing this using df.query instead??\n",
    "df[df.Location.str.contains('NY',na=False)]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Now *count* all of the breweries in New York state"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 504,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Sixpoint Craft Ales              24\n",
       "Matt Brewing Company             13\n",
       "Brooklyn Brewery                  6\n",
       "Evil Twin Brewing                 5\n",
       "Blue Point Brewing Company        4\n",
       "Butternuts Beer and Ale           4\n",
       "The Bronx Brewery                 3\n",
       "KelSo Beer Company                3\n",
       "Chatham Brewing                   2\n",
       "Montauk Brewing Company           2\n",
       "Bomb Beer Company                 2\n",
       "Upstate Brewing Company           2\n",
       "Newburgh Brewing Company          1\n",
       "Southampton Publick House         1\n",
       "The Manhattan Brewing Company     1\n",
       "Dundee Brewing Company            1\n",
       "Name: Brewery, dtype: int64"
      ]
     },
     "execution_count": 504,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "newyork_df = df[df.Location.str.contains('NY',na=False)]\n",
    "newyork_df.Brewery.value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Measuring International Bitterness Units\n",
    "\n",
    "## Display all of the IPAs\n",
    "\n",
    "Include American IPAs, Imperial IPAs, and anything else with \"IPA in it.\"\n",
    "\n",
    "IPA stands for [India Pale Ale](https://www.bonappetit.com/story/ipa-beer-styles), and is probably the most popular kind of beer in the US for people who are drinking [craft beer](https://www.craftbeer.com/beer/what-is-craft-beer)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 505,
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
       "      <th>Beer</th>\n",
       "      <th>Brewery</th>\n",
       "      <th>Location</th>\n",
       "      <th>Style</th>\n",
       "      <th>Size</th>\n",
       "      <th>ABV</th>\n",
       "      <th>IBUs</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Get Together</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.5</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Citra Ass Down</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>8.0</td>\n",
       "      <td>68</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Rico Sauvin</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>7.6</td>\n",
       "      <td>68</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Pile of Face</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.0</td>\n",
       "      <td>65</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>Habitus (2014)</td>\n",
       "      <td>Mike Hess Brewing Company</td>\n",
       "      <td>San Diego, CA</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>8.0</td>\n",
       "      <td>100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2403</th>\n",
       "      <td>Abrasive Ale</td>\n",
       "      <td>Surly Brewing Company</td>\n",
       "      <td>Brooklyn Center, MN</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>9.7</td>\n",
       "      <td>120</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2406</th>\n",
       "      <td>Furious</td>\n",
       "      <td>Surly Brewing Company</td>\n",
       "      <td>Brooklyn Center, MN</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.2</td>\n",
       "      <td>99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2408</th>\n",
       "      <td>Brew Free! or Die IPA</td>\n",
       "      <td>21st Amendment Brewery</td>\n",
       "      <td>San Francisco, CA</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>7.0</td>\n",
       "      <td>65</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2412</th>\n",
       "      <td>GUBNA Imperial IPA</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>9.9</td>\n",
       "      <td>100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2414</th>\n",
       "      <td>Gordon Ale (2009)</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>8.7</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>571 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                       Beer                    Brewery             Location  \\\n",
       "0              Get Together          NorthGate Brewing      Minneapolis, MN   \n",
       "6            Citra Ass Down  Against the Grain Brewery       Louisville, KY   \n",
       "14              Rico Sauvin  Against the Grain Brewery       Louisville, KY   \n",
       "17             Pile of Face  Against the Grain Brewery       Louisville, KY   \n",
       "24           Habitus (2014)  Mike Hess Brewing Company        San Diego, CA   \n",
       "...                     ...                        ...                  ...   \n",
       "2403           Abrasive Ale      Surly Brewing Company  Brooklyn Center, MN   \n",
       "2406                Furious      Surly Brewing Company  Brooklyn Center, MN   \n",
       "2408  Brew Free! or Die IPA     21st Amendment Brewery    San Francisco, CA   \n",
       "2412     GUBNA Imperial IPA        Oskar Blues Brewery         Longmont, CO   \n",
       "2414      Gordon Ale (2009)        Oskar Blues Brewery         Longmont, CO   \n",
       "\n",
       "                               Style    Size  ABV IBUs  \n",
       "0                       American IPA  16 oz.  4.5   50  \n",
       "6     American Double / Imperial IPA  16 oz.  8.0   68  \n",
       "14    American Double / Imperial IPA  16 oz.  7.6   68  \n",
       "17                      American IPA  16 oz.  6.0   65  \n",
       "24    American Double / Imperial IPA  16 oz.  8.0  100  \n",
       "...                              ...     ...  ...  ...  \n",
       "2403  American Double / Imperial IPA  16 oz.  9.7  120  \n",
       "2406                    American IPA  16 oz.  6.2   99  \n",
       "2408                    American IPA  12 oz.  7.0   65  \n",
       "2412  American Double / Imperial IPA  12 oz.  9.9  100  \n",
       "2414  American Double / Imperial IPA  12 oz.  8.7   85  \n",
       "\n",
       "[571 rows x 7 columns]"
      ]
     },
     "execution_count": 505,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.Style.str.contains('IPA',na=False)]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "IPAs are usually pretty hoppy and bitter (although I guess hazy IPAs and session IPAs are changing that since I first made this homework!). IBU stands for [International Bitterness Unit](http://www.thebrewenthusiast.com/ibus/), and while a lot of places like to brag about having the most bitter beer (it's an American thing!), IBUs don't necessary *mean anything*.\n",
    "\n",
    "Let's look at how different beers have different IBU measurements."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Try to get the average IBU measurement across all beers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 506,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "could not convert string to float: 'Does not apply'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "File \u001b[0;32m~/.pyenv/versions/3.10.3/lib/python3.10/site-packages/pandas/core/nanops.py:752\u001b[0m, in \u001b[0;36mnanmedian\u001b[0;34m(values, axis, skipna, mask)\u001b[0m\n\u001b[1;32m    751\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 752\u001b[0m     values \u001b[38;5;241m=\u001b[39m \u001b[43mvalues\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mastype\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mf8\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[1;32m    753\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m err:\n\u001b[1;32m    754\u001b[0m     \u001b[38;5;66;03m# e.g. \"could not convert string to float: 'a'\"\u001b[39;00m\n",
      "\u001b[0;31mValueError\u001b[0m: could not convert string to float: 'Does not apply'",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[0;32mIn [506]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mdf\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mIBUs\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mmedian\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/.pyenv/versions/3.10.3/lib/python3.10/site-packages/pandas/core/generic.py:11187\u001b[0m, in \u001b[0;36mNDFrame._add_numeric_operations.<locals>.median\u001b[0;34m(self, axis, skipna, level, numeric_only, **kwargs)\u001b[0m\n\u001b[1;32m  11169\u001b[0m \u001b[38;5;129m@doc\u001b[39m(\n\u001b[1;32m  11170\u001b[0m     _num_doc,\n\u001b[1;32m  11171\u001b[0m     desc\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mReturn the median of the values over the requested axis.\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m  11185\u001b[0m     \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs,\n\u001b[1;32m  11186\u001b[0m ):\n\u001b[0;32m> 11187\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mNDFrame\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mmedian\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43maxis\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mskipna\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mlevel\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mnumeric_only\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/.pyenv/versions/3.10.3/lib/python3.10/site-packages/pandas/core/generic.py:10699\u001b[0m, in \u001b[0;36mNDFrame.median\u001b[0;34m(self, axis, skipna, level, numeric_only, **kwargs)\u001b[0m\n\u001b[1;32m  10691\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mmedian\u001b[39m(\n\u001b[1;32m  10692\u001b[0m     \u001b[38;5;28mself\u001b[39m,\n\u001b[1;32m  10693\u001b[0m     axis: Axis \u001b[38;5;241m|\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;241m|\u001b[39m lib\u001b[38;5;241m.\u001b[39mNoDefault \u001b[38;5;241m=\u001b[39m lib\u001b[38;5;241m.\u001b[39mno_default,\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m  10697\u001b[0m     \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs,\n\u001b[1;32m  10698\u001b[0m ) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m Series \u001b[38;5;241m|\u001b[39m \u001b[38;5;28mfloat\u001b[39m:\n\u001b[0;32m> 10699\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_stat_function\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m  10700\u001b[0m \u001b[43m        \u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mmedian\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mnanops\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mnanmedian\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43maxis\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mskipna\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mlevel\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mnumeric_only\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\n\u001b[1;32m  10701\u001b[0m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/.pyenv/versions/3.10.3/lib/python3.10/site-packages/pandas/core/generic.py:10639\u001b[0m, in \u001b[0;36mNDFrame._stat_function\u001b[0;34m(self, name, func, axis, skipna, level, numeric_only, **kwargs)\u001b[0m\n\u001b[1;32m  10629\u001b[0m     warnings\u001b[38;5;241m.\u001b[39mwarn(\n\u001b[1;32m  10630\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mUsing the level keyword in DataFrame and Series aggregations is \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m  10631\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdeprecated and will be removed in a future version. Use groupby \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m  10634\u001b[0m         stacklevel\u001b[38;5;241m=\u001b[39mfind_stack_level(),\n\u001b[1;32m  10635\u001b[0m     )\n\u001b[1;32m  10636\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_agg_by_level(\n\u001b[1;32m  10637\u001b[0m         name, axis\u001b[38;5;241m=\u001b[39maxis, level\u001b[38;5;241m=\u001b[39mlevel, skipna\u001b[38;5;241m=\u001b[39mskipna, numeric_only\u001b[38;5;241m=\u001b[39mnumeric_only\n\u001b[1;32m  10638\u001b[0m     )\n\u001b[0;32m> 10639\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_reduce\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m  10640\u001b[0m \u001b[43m    \u001b[49m\u001b[43mfunc\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mname\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mname\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43maxis\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43maxis\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mskipna\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mskipna\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mnumeric_only\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mnumeric_only\u001b[49m\n\u001b[1;32m  10641\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/.pyenv/versions/3.10.3/lib/python3.10/site-packages/pandas/core/series.py:4471\u001b[0m, in \u001b[0;36mSeries._reduce\u001b[0;34m(self, op, name, axis, skipna, numeric_only, filter_type, **kwds)\u001b[0m\n\u001b[1;32m   4467\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mNotImplementedError\u001b[39;00m(\n\u001b[1;32m   4468\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mSeries.\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mname\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m does not implement \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mkwd_name\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m   4469\u001b[0m     )\n\u001b[1;32m   4470\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m np\u001b[38;5;241m.\u001b[39merrstate(\u001b[38;5;28mall\u001b[39m\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mignore\u001b[39m\u001b[38;5;124m\"\u001b[39m):\n\u001b[0;32m-> 4471\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mop\u001b[49m\u001b[43m(\u001b[49m\u001b[43mdelegate\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mskipna\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mskipna\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwds\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/.pyenv/versions/3.10.3/lib/python3.10/site-packages/pandas/core/nanops.py:155\u001b[0m, in \u001b[0;36mbottleneck_switch.__call__.<locals>.f\u001b[0;34m(values, axis, skipna, **kwds)\u001b[0m\n\u001b[1;32m    153\u001b[0m         result \u001b[38;5;241m=\u001b[39m alt(values, axis\u001b[38;5;241m=\u001b[39maxis, skipna\u001b[38;5;241m=\u001b[39mskipna, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwds)\n\u001b[1;32m    154\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m--> 155\u001b[0m     result \u001b[38;5;241m=\u001b[39m \u001b[43malt\u001b[49m\u001b[43m(\u001b[49m\u001b[43mvalues\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43maxis\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43maxis\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mskipna\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mskipna\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwds\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    157\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m result\n",
      "File \u001b[0;32m~/.pyenv/versions/3.10.3/lib/python3.10/site-packages/pandas/core/nanops.py:755\u001b[0m, in \u001b[0;36mnanmedian\u001b[0;34m(values, axis, skipna, mask)\u001b[0m\n\u001b[1;32m    752\u001b[0m     values \u001b[38;5;241m=\u001b[39m values\u001b[38;5;241m.\u001b[39mastype(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mf8\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m    753\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m err:\n\u001b[1;32m    754\u001b[0m     \u001b[38;5;66;03m# e.g. \"could not convert string to float: 'a'\"\u001b[39;00m\n\u001b[0;32m--> 755\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mTypeError\u001b[39;00m(\u001b[38;5;28mstr\u001b[39m(err)) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01merr\u001b[39;00m\n\u001b[1;32m    756\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m mask \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m    757\u001b[0m     values[mask] \u001b[38;5;241m=\u001b[39m np\u001b[38;5;241m.\u001b[39mnan\n",
      "\u001b[0;31mTypeError\u001b[0m: could not convert string to float: 'Does not apply'"
     ]
    }
   ],
   "source": [
    "df.IBUs.median()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Oh no, it doesn't work!\n",
    "\n",
    "It looks like some of those values *aren't numbers*. There are two ways to fix this:\n",
    "\n",
    "1. Do the `.replace` and `np.nan` thing we did in class. Then convert the column to a number. This is boring.\n",
    "2. When you're reading in your csv, there [is an option called `na_values`](http://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.read_csv.html). You can give it a list of **numbers or strings to count as `NaN`**. It's a lot easier than doing the `np.nan` thing, although you'll need to go add it up top and run all of your cells again.\n",
    "\n",
    "- *Tip: Make sure you're giving `na_values` a LIST, not just a string*\n",
    "\n",
    "### Now try to get the average IBUs again"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 507,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "35.0"
      ]
     },
     "execution_count": 507,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#import numpy as np\n",
    "df.IBUs = df.IBUs.replace('Does not apply', np.nan)\n",
    "df.IBUs.median()\n"
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
    "## Draw the distribution of IBU measurements, but with *twenty* bins instead of the default of 10\n",
    "\n",
    "- *Tip: Every time I ask for a distribution, I'm looking for a histogram*\n",
    "- *Tip: Use the `?` to get all of the options for building a histogram*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 508,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 508,
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
    "df.IBUs.hist(bins = 20)"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Hm, Interesting distribution. List all of the beers with IBUs above the 75th percentile\n",
    "\n",
    "- *Tip: There's a single that gives you the 25/50/75th percentile*\n",
    "- *Tip: You can just manually type the number when you list those beers*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 512,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "64.0"
      ]
     },
     "execution_count": 512,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.IBUs.quantile(0.75)\n",
    "\n",
    "# Initially I did this:\n",
    "# df.IBUs.quantile(0.75) --> unsupported operand type(s) for -: 'str' and 'str'\n",
    "# df.IBUs = df.IBUs.astype(int) --> Cannot convert cannot convert float NaN to integer\n",
    "# To eliminate those cases? using --> df.query(\"IBUs.isna()\")\n",
    "# Thats 1011 rows! Almost half the total beers\n",
    "# df = df.dropna(subset=['IBUs'])\n",
    "# df.IBUs = df.IBUs.astype(int)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 513,
   "metadata": {
    "scrolled": true
   },
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
       "      <th>Beer</th>\n",
       "      <th>Brewery</th>\n",
       "      <th>Location</th>\n",
       "      <th>Style</th>\n",
       "      <th>Size</th>\n",
       "      <th>ABV</th>\n",
       "      <th>IBUs</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Citra Ass Down</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>8.0</td>\n",
       "      <td>68</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>London Balling</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>English Barleywine</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>12.5</td>\n",
       "      <td>80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Rico Sauvin</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>7.6</td>\n",
       "      <td>68</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Pile of Face</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.0</td>\n",
       "      <td>65</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>Excess IPL</td>\n",
       "      <td>Jack's Abby Craft Lagers</td>\n",
       "      <td>Framingham, MA</td>\n",
       "      <td>American India Pale Lager</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>7.2</td>\n",
       "      <td>80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2408</th>\n",
       "      <td>Brew Free! or Die IPA</td>\n",
       "      <td>21st Amendment Brewery</td>\n",
       "      <td>San Francisco, CA</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>7.0</td>\n",
       "      <td>65</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2410</th>\n",
       "      <td>Ten Fidy Imperial Stout</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>Russian Imperial Stout</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>9.9</td>\n",
       "      <td>98</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2412</th>\n",
       "      <td>GUBNA Imperial IPA</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>9.9</td>\n",
       "      <td>100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2414</th>\n",
       "      <td>Gordon Ale (2009)</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>8.7</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2415</th>\n",
       "      <td>Dale's Pale Ale</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>American Pale Ale (APA)</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>6.5</td>\n",
       "      <td>65</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>346 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                         Beer                    Brewery           Location  \\\n",
       "6              Citra Ass Down  Against the Grain Brewery     Louisville, KY   \n",
       "7              London Balling  Against the Grain Brewery     Louisville, KY   \n",
       "14                Rico Sauvin  Against the Grain Brewery     Louisville, KY   \n",
       "17               Pile of Face  Against the Grain Brewery     Louisville, KY   \n",
       "21                 Excess IPL   Jack's Abby Craft Lagers     Framingham, MA   \n",
       "...                       ...                        ...                ...   \n",
       "2408    Brew Free! or Die IPA     21st Amendment Brewery  San Francisco, CA   \n",
       "2410  Ten Fidy Imperial Stout        Oskar Blues Brewery       Longmont, CO   \n",
       "2412       GUBNA Imperial IPA        Oskar Blues Brewery       Longmont, CO   \n",
       "2414        Gordon Ale (2009)        Oskar Blues Brewery       Longmont, CO   \n",
       "2415          Dale's Pale Ale        Oskar Blues Brewery       Longmont, CO   \n",
       "\n",
       "                               Style    Size   ABV  IBUs  \n",
       "6     American Double / Imperial IPA  16 oz.   8.0    68  \n",
       "7                 English Barleywine  16 oz.  12.5    80  \n",
       "14    American Double / Imperial IPA  16 oz.   7.6    68  \n",
       "17                      American IPA  16 oz.   6.0    65  \n",
       "21         American India Pale Lager  16 oz.   7.2    80  \n",
       "...                              ...     ...   ...   ...  \n",
       "2408                    American IPA  12 oz.   7.0    65  \n",
       "2410          Russian Imperial Stout  12 oz.   9.9    98  \n",
       "2412  American Double / Imperial IPA  12 oz.   9.9   100  \n",
       "2414  American Double / Imperial IPA  12 oz.   8.7    85  \n",
       "2415         American Pale Ale (APA)  12 oz.   6.5    65  \n",
       "\n",
       "[346 rows x 7 columns]"
      ]
     },
     "execution_count": 513,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.IBUs > 64]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## List all of the beers with IBUs below the 25th percentile"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 514,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "21.0"
      ]
     },
     "execution_count": 514,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.IBUs.quantile(0.25)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 515,
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
       "      <th>Beer</th>\n",
       "      <th>Brewery</th>\n",
       "      <th>Location</th>\n",
       "      <th>Style</th>\n",
       "      <th>Size</th>\n",
       "      <th>ABV</th>\n",
       "      <th>IBUs</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Wall's End</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>English Brown Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.8</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Sho'nuff</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>Belgian Pale Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.0</td>\n",
       "      <td>13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Bloody Show</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>American Pilsner</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.5</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>The Brown Note</td>\n",
       "      <td>Against the Grain Brewery</td>\n",
       "      <td>Louisville, KY</td>\n",
       "      <td>English Brown Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.0</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>House Lager</td>\n",
       "      <td>Jack's Abby Craft Lagers</td>\n",
       "      <td>Framingham, MA</td>\n",
       "      <td>Keller Bier / Zwickel Bier</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.2</td>\n",
       "      <td>18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2372</th>\n",
       "      <td>Bombshell Blonde</td>\n",
       "      <td>Southern Star Brewing Company</td>\n",
       "      <td>Conroe, TX</td>\n",
       "      <td>American Blonde Ale</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>5.0</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2385</th>\n",
       "      <td>Bikini Blonde Lager</td>\n",
       "      <td>Maui Brewing Company</td>\n",
       "      <td>Lahaina, HI</td>\n",
       "      <td>Munich Helles Lager</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>4.5</td>\n",
       "      <td>18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2396</th>\n",
       "      <td>Royal Weisse Ale</td>\n",
       "      <td>Sly Fox Brewing Company</td>\n",
       "      <td>Pottstown, PA</td>\n",
       "      <td>Hefeweizen</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>5.6</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2404</th>\n",
       "      <td>Hell</td>\n",
       "      <td>Surly Brewing Company</td>\n",
       "      <td>Brooklyn Center, MN</td>\n",
       "      <td>Keller Bier / Zwickel Bier</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>5.1</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2409</th>\n",
       "      <td>Hell or High Watermelon Wheat</td>\n",
       "      <td>21st Amendment Brewery</td>\n",
       "      <td>San Francisco, CA</td>\n",
       "      <td>Fruit / Vegetable Beer</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>4.9</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>338 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                               Beer                        Brewery  \\\n",
       "2                        Wall's End              NorthGate Brewing   \n",
       "12                         Sho'nuff      Against the Grain Brewery   \n",
       "13                      Bloody Show      Against the Grain Brewery   \n",
       "18                   The Brown Note      Against the Grain Brewery   \n",
       "19                      House Lager       Jack's Abby Craft Lagers   \n",
       "...                             ...                            ...   \n",
       "2372               Bombshell Blonde  Southern Star Brewing Company   \n",
       "2385            Bikini Blonde Lager           Maui Brewing Company   \n",
       "2396               Royal Weisse Ale        Sly Fox Brewing Company   \n",
       "2404                           Hell          Surly Brewing Company   \n",
       "2409  Hell or High Watermelon Wheat         21st Amendment Brewery   \n",
       "\n",
       "                 Location                       Style    Size  ABV  IBUs  \n",
       "2         Minneapolis, MN           English Brown Ale  16 oz.  4.8    19  \n",
       "12         Louisville, KY            Belgian Pale Ale  16 oz.  4.0    13  \n",
       "13         Louisville, KY            American Pilsner  16 oz.  5.5    17  \n",
       "18         Louisville, KY           English Brown Ale  16 oz.  5.0    20  \n",
       "19         Framingham, MA  Keller Bier / Zwickel Bier  16 oz.  5.2    18  \n",
       "...                   ...                         ...     ...  ...   ...  \n",
       "2372           Conroe, TX         American Blonde Ale  12 oz.  5.0    20  \n",
       "2385          Lahaina, HI         Munich Helles Lager  12 oz.  4.5    18  \n",
       "2396        Pottstown, PA                  Hefeweizen  12 oz.  5.6    11  \n",
       "2404  Brooklyn Center, MN  Keller Bier / Zwickel Bier  16 oz.  5.1    20  \n",
       "2409    San Francisco, CA      Fruit / Vegetable Beer  12 oz.  4.9    17  \n",
       "\n",
       "[338 rows x 7 columns]"
      ]
     },
     "execution_count": 515,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.IBUs < 21]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## List the median IBUs of each type of beer. Graph it.\n",
    "\n",
    "Put the highest at the top, and the missing ones at the bottom.\n",
    "\n",
    "- Tip: Look at the options for `sort_values` to figure out the `NaN` thing. The `?` probably won't help you here."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 516,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Style\n",
       "American Barleywine                   96.0\n",
       "Russian Imperial Stout                94.0\n",
       "American Double / Imperial IPA        91.0\n",
       "American Double / Imperial Pilsner    85.0\n",
       "American Black Ale                    73.0\n",
       "                                      ... \n",
       "Herbed / Spiced Beer                  15.0\n",
       "Light Lager                           12.0\n",
       "Gose                                  10.0\n",
       "American Adjunct Lager                 9.0\n",
       "Berliner Weissbier                     8.0\n",
       "Name: IBUs, Length: 90, dtype: float64"
      ]
     },
     "execution_count": 516,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby(by = 'Style').IBUs.median().sort_values(ascending = False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 517,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Style'>"
      ]
     },
     "execution_count": 517,
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
    "df.groupby(by = 'Style').IBUs.median().sort_values(ascending = False).plot()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Hmmmm, it looks like they are generally different styles. What are the most common 5 styles of high-IBU beer vs. low-IBU beer?\n",
    "\n",
    "- *Tip: You'll want to think about it in three pieces - filtering to only find the specific beers beers, then finding out what the most common styles are, then getting the top 5.*\n",
    "- *Tip: You CANNOT do this in one command. It's going to be one command for the high and one for the low.*\n",
    "- *Tip: \"High IBU\" means higher than 75th percentile, \"Low IBU\" is under 25th percentile*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 518,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "American IPA                      195\n",
       "American Double / Imperial IPA     72\n",
       "American Pale Ale (APA)            18\n",
       "American Black Ale                 15\n",
       "American Strong Ale                 9\n",
       "Name: Style, dtype: int64"
      ]
     },
     "execution_count": 518,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query(\"IBUs > 64\").sort_values(by='IBUs').Style.value_counts().head(5)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 519,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "American Pale Wheat Ale    43\n",
       "American Blonde Ale        36\n",
       "Fruit / Vegetable Beer     28\n",
       "Hefeweizen                 21\n",
       "Witbier                    20\n",
       "Name: Style, dtype: int64"
      ]
     },
     "execution_count": 519,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query(\"IBUs < 21\").sort_values(by='IBUs').Style.value_counts().head(5)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Get the average IBU of \"Witbier\", \"Hefeweizen\" and \"American Pale Wheat Ale\" styles\n",
    "\n",
    "I'm counting these as wheat beers. If you see any other wheat beer categories, feel free to include them. I want ONE measurement and ONE graph, not three separate ones. And 20 to 30 bins in the histogram, please.\n",
    "\n",
    "- *Tip: I hope that `isin` is in your toolbox*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 520,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/var/folders/d4/23ptlp_n23v3pg6pl6h56x600000gn/T/ipykernel_28688/2162323889.py:1: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  df['wheat_beers'] = df['Style'].isin(['Witbier', 'Hefeweizen', 'American Pale Wheat Ale'])\n"
     ]
    },
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
       "      <th>Beer</th>\n",
       "      <th>Brewery</th>\n",
       "      <th>Location</th>\n",
       "      <th>Style</th>\n",
       "      <th>Size</th>\n",
       "      <th>ABV</th>\n",
       "      <th>IBUs</th>\n",
       "      <th>wheat_beers</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Get Together</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>American IPA</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.5</td>\n",
       "      <td>50</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Maggie's Leap</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>Milk / Sweet Stout</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.9</td>\n",
       "      <td>26</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Wall's End</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>English Brown Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>4.8</td>\n",
       "      <td>19</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Pumpion</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>Pumpkin Ale</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.0</td>\n",
       "      <td>38</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Stronghold</td>\n",
       "      <td>NorthGate Brewing</td>\n",
       "      <td>Minneapolis, MN</td>\n",
       "      <td>American Porter</td>\n",
       "      <td>16 oz.</td>\n",
       "      <td>6.0</td>\n",
       "      <td>25</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2411</th>\n",
       "      <td>Mama's Little Yella Pils</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>Czech Pilsener</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>5.3</td>\n",
       "      <td>35</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2412</th>\n",
       "      <td>GUBNA Imperial IPA</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>9.9</td>\n",
       "      <td>100</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2413</th>\n",
       "      <td>Old Chub</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>Scottish Ale</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>8.0</td>\n",
       "      <td>35</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2414</th>\n",
       "      <td>Gordon Ale (2009)</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>American Double / Imperial IPA</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>8.7</td>\n",
       "      <td>85</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2415</th>\n",
       "      <td>Dale's Pale Ale</td>\n",
       "      <td>Oskar Blues Brewery</td>\n",
       "      <td>Longmont, CO</td>\n",
       "      <td>American Pale Ale (APA)</td>\n",
       "      <td>12 oz.</td>\n",
       "      <td>6.5</td>\n",
       "      <td>65</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1405 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                          Beer              Brewery         Location  \\\n",
       "0                 Get Together    NorthGate Brewing  Minneapolis, MN   \n",
       "1                Maggie's Leap    NorthGate Brewing  Minneapolis, MN   \n",
       "2                   Wall's End    NorthGate Brewing  Minneapolis, MN   \n",
       "3                      Pumpion    NorthGate Brewing  Minneapolis, MN   \n",
       "4                   Stronghold    NorthGate Brewing  Minneapolis, MN   \n",
       "...                        ...                  ...              ...   \n",
       "2411  Mama's Little Yella Pils  Oskar Blues Brewery     Longmont, CO   \n",
       "2412        GUBNA Imperial IPA  Oskar Blues Brewery     Longmont, CO   \n",
       "2413                  Old Chub  Oskar Blues Brewery     Longmont, CO   \n",
       "2414         Gordon Ale (2009)  Oskar Blues Brewery     Longmont, CO   \n",
       "2415           Dale's Pale Ale  Oskar Blues Brewery     Longmont, CO   \n",
       "\n",
       "                               Style    Size  ABV  IBUs  wheat_beers  \n",
       "0                       American IPA  16 oz.  4.5    50        False  \n",
       "1                 Milk / Sweet Stout  16 oz.  4.9    26        False  \n",
       "2                  English Brown Ale  16 oz.  4.8    19        False  \n",
       "3                        Pumpkin Ale  16 oz.  6.0    38        False  \n",
       "4                    American Porter  16 oz.  6.0    25        False  \n",
       "...                              ...     ...  ...   ...          ...  \n",
       "2411                  Czech Pilsener  12 oz.  5.3    35        False  \n",
       "2412  American Double / Imperial IPA  12 oz.  9.9   100        False  \n",
       "2413                    Scottish Ale  12 oz.  8.0    35        False  \n",
       "2414  American Double / Imperial IPA  12 oz.  8.7    85        False  \n",
       "2415         American Pale Ale (APA)  12 oz.  6.5    65        False  \n",
       "\n",
       "[1405 rows x 8 columns]"
      ]
     },
     "execution_count": 520,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['wheat_beers'] = df['Style'].isin(['Witbier', 'Hefeweizen', 'American Pale Wheat Ale'])\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 521,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "18.0"
      ]
     },
     "execution_count": 521,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query(\"wheat_beers == True\").IBUs.median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Why this doesn't work?\n",
    "df[df[\"wheat_beers\"] == 'True']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Draw a histogram of the IBUs of those beers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 522,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 522,
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
    "df.query(\"wheat_beers == True\").IBUs.hist()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Get the average IBU of any style with \"IPA\" in it (also draw a histogram)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 529,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/var/folders/d4/23ptlp_n23v3pg6pl6h56x600000gn/T/ipykernel_28688/1342644876.py:1: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  df['IPA'] = df.Style.str.contains(\"IPA\")\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "70.0"
      ]
     },
     "execution_count": 529,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['IPA'] = df.Style.str.contains(\"IPA\")\n",
    "df.query(\"IPA == True\").IBUs.median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 530,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 530,
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
    "df.query(\"IPA == True\").IBUs.hist()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Plot those two histograms on top of one another\n",
    "\n",
    "To plot two plots on top of one another, you *might* just be able to plot twice in the same cell. It depends on your version of pandas/matplotlib! If it doesn't work, you'll need do two steps.\n",
    "\n",
    "1. First, you make a plot using `plot` or `hist`, and you save it into a variable called `ax`.\n",
    "2. You draw your second graph using `plot` or `hist`, and send `ax=ax` to it as a parameter.\n",
    "\n",
    "It would look something like this:\n",
    "\n",
    "```python\n",
    "ax = df.plot(....)\n",
    "df.plot(ax=ax, ....)\n",
    "``` \n",
    "\n",
    "And then youull get two plots on top of each other. They won't be perfect because the bins won't line up without extra work, but it's fine!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 531,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 531,
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
    "df.query(\"wheat_beers == True\").IBUs.hist()\n",
    "df.query(\"IPA == True\").IBUs.hist()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Compare the ABV of wheat beers vs. IPAs : their IBUs were really different, but how about their alcohol percentage?\n",
    "\n",
    "Wheat beers might include witbier, hefeweizen, American Pale Wheat Ale, and anything else you think is wheaty. IPAs probably have \"IPA\" in their name."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 532,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.0"
      ]
     },
     "execution_count": 532,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query(\"wheat_beers == True\").ABV.median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 533,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6.8"
      ]
     },
     "execution_count": 533,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query(\"IPA == True\").ABV.median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 548,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 548,
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
    "df.query(\"wheat_beers == True\").ABV.hist()\n",
    "df.query(\"IPA == True\").ABV.hist()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## Good work!\n",
    "\n",
    "For making it this far, your reward is my recommendation for Athletic Brewing Co.'s products as the best non-alcoholic beer on the market. Their Run Wild IPA and Upside Dawn are both very solid."
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

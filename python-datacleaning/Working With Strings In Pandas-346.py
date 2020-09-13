## 1. Introduction ##

world_dev = pd.read_csv("World_dev.csv")
col_renaming = {'SourceOfMostRecentIncomeAndExpenditureData': 'IESurvey'}
merged=pd.merge(happiness2015,world_dev,left_on='Country',right_on='ShortName',how='left')
merged.head()
merged=merged.rename(columns=col_renaming)

## 2. Using Apply to Transform Strings ##

def extract_last_word(element):
    element=str(element)
    splitted=element.split()
    return splitted[-1]

merged['Currency Apply']=merged['CurrencyUnit'].apply(extract_last_word)
merged['Currency Apply'].head()

## 3. Vectorized String Methods Overview ##

merged['Currency Vectorized']=merged['CurrencyUnit'].str.split().str.get(-1)
merged['Currency Vectorized'].head()

## 4. Exploring Missing Values with Vectorized String Methods ##

lengths=merged['CurrencyUnit'].str.len()
value_counts=lengths.value_counts(dropna=False)

## 5. Finding Specific Words in Strings ##

pattern = r"[Nn]ational accounts"
national_accounts=merged['SpecialNotes'].str.contains(pattern)
national_accounts.head()
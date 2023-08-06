"""
Python package that allows users to view information about their senators and the industries that fund them.

This module uses the OpenSecrets and ProPublica APIs and scraps the OpenSecrets website to return information about
the top 20 industries that fund the US Congress and the senators who have received the most funding from these
industries.
"""

from json.decoder import JSONDecodeError
import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml


# Web-scrapping the OpenSecrets Website for the Top 20 Industries that have spent the most on Federal Lobbying
def top_20_industries_ids(year='a'):
    """
    Extracts the Top 20 Industries that have spent the most on Federal Lobbying from
    https://www.opensecrets.org/federal-lobbying/industries.

    Parameters
    ----------
    year : str, optional
        Specific year (1998 - 2021) for which to retrieve the data for (the default is 'a' which would
        return the total amount of money spent on Federal Lobbying across all years from 1998 - 2021).

    Returns
    -------
    pandas.DataFrame
        Dataframe containing the Top 20 Industries that have spent the most on Federal Lobbying, the amount of
        money they have each spent, and their unique Industry IDs.

    Examples
    --------
    >>> top_20_industries_ids()
    [   Industry	                        Total	        IDs
    0	Pharmaceuticals/Health Products	    $4,990,257,367	H04
    1	Insurance	                        $3,210,878,113	F09
    2	Electronics Mfg & Equip	            $2,795,736,767	B12
    3	Electric Utilities	                $2,757,808,440	E08
    4	Business Associations	            $2,623,983,096	N00
    5	Oil & Gas	                        $2,489,418,498	E01
    6	Hospitals/Nursing Homes	            $2,025,651,797	H02
    7	Misc Manufacturing & Distributing	$2,008,839,171	N15
    8	Education	                        $1,902,258,320	W04
    9	Securities & Investment	            $1,897,760,970	F07
    10	Civil Servants/Public Officials	    $1,887,599,161	W03
    11	Telecom Services	                $1,883,769,733	B09
    12	Real Estate	                        $1,874,450,800	F10
    13	Air Transport	                    $1,730,349,996	M01
    14	Health Professionals	            $1,712,045,500	H01
    15	Health Services/HMOs	            $1,405,134,830	H03
    16	Automotive	                        $1,322,462,732	M02
    17	TV/Movies/Music	                    $1,301,018,584	B02
    18	Misc Issues	                        $1,247,693,549	Q10
    19	Defense Aerospace	                $1,232,991,613	D01     ]

    """
    url = ('https://www.opensecrets.org/federal-lobbying/industries?cycle=' + str(year))
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    # Extracting all the URLs from the website
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    # Extracting URLs that contain the unique industry IDs corresponding to each of the Top 20
    url_ids = [url for url in urls if 'federal-lobbying/industries/summary' in url]
    url_ids_df = pd.DataFrame(url_ids)
    # Splitting the IDs from the rest of the URL
    ids = url_ids_df[0].str.split('id=')
    # Extracting list of unique industry IDs corresponding to each industry
    industry_id = []
    for i in range(len(ids)):
        industry_id.append(ids[i][1])
    # Extracting table of Top 20 Industries that have spent the most on Federal Lobbying along with the respective 
    # amounts they have spent 
    df = pd.read_html(html.text)[0][:20]
    # Adding a column to the table which contains the industry IDs corresponding to each Industry
    df['IDs'] = industry_id
    return df


class ProPublicaAPIKey:
    """
    All functions that require the ProPublica API Key.

    Attributes
    ----------
    propublica_api_key: str
        ProPublica API Key to use ProPublica's Congress API. The API Key can be requested from
        https://www.propublica.org/datastore/api/propublica-congress-api.

    Methods
    ----------
    senate_members (congress_sitting=117)
        Provides a pandas Dataframe containing all the Senators from a particular sitting of Congress

        """

    def __init__(self, propublica_api_key):
        self.propublica_api_key = propublica_api_key

    def senate_members(self, congress_sitting=117):
        """
        Uses the ProPublica API to extract a list of Senators.

        Parameters
        ----------
        congress_sitting: int, optional
            Allows the user to specify senators from which sitting of Congress (80-117) they would like
            information about (the default is 117, which would return all the senators in the 117th Congress).

        Returns
        -------
        pandas.DataFrame
            Pandas DataFrame containing the names, state and CRP IDs of all senators in a particular sitting of
            Congress.

        Examples
        --------
        >>> ProPublica = ProPublicaAPIKey('insert ProPublica API Key here')
        >>> ProPublica.senate_members()
        [	first_name	middle_name	last_name	state	crp_id
        0	Tammy	    None	    Baldwin	    WI	    N00004367
        1	John	    None	    Barrasso	WY	    N00006236
        2	Michael	    None	    Bennet	    CO	    N00030608
        3	Marsha	    None	    Blackburn	TN	    N00003105
        4	Richard	    None	    Blumenthal	CT	    N00031685
        ...	...	        ...	        ...	        ...	    ...
        97	Elizabeth	None	    Warren	    MA	    N00033492
        98	Sheldon	    None	    Whitehouse	RI	    N00027533
        99	Roger	    None	    Wicker	    MS	    N00003280
        100	Ron	        None	    Wyden	    OR	    N00007724
        101	Todd	    None	    Young	    IN	    N00030670
        102 rows × 5 columns    ]

        """
        # Calling the ProPublica Congress API to extract information about senators in a particular sitting of Congress
        headers = {'X-API-Key': self.propublica_api_key}
        r = requests.get('https://api.propublica.org/congress/v1/' + str(congress_sitting) + '/senate/members.json',
                         headers=headers)
        try:
            senate_members = r.json()
            senate_members_df = pd.DataFrame(senate_members['results'][0]['members'])
            # Selecting relevant columns to return
            new_cols = ['first_name', 'middle_name', 'last_name', 'state', 'crp_id']
            result = senate_members_df[new_cols]
            return result
        except KeyError:
            print(f'Error: Unexpected content returned from API. Check if API Key is correct.')


class OpenSecretsAPIKey:
    """
    All functions that require the OpenSecrets API Key.

    Attributes
    ----------
    opensecrets_api_key: str
        OpenSecrets API Key to use ProPublica's Congress API. The API Key can be requested from
        https://www.opensecrets.org/api/admin/index.php?function=signup.

    Methods
    ----------
    top_senators_each_industry(propublica_api_key, industry_id, **kwargs)
        Provides a DataFrame of senators ranked according to who has received the most amount of funding from a
        particular industry

    """

    def __init__(self, opensecrets_api_key):
        self.opensecrets_api_key = opensecrets_api_key

    def top_senators_each_industry(self, propublica_api_key, industry_id='H04', **kwargs):
        """
        Uses the OpenSecretsAPI and ProPublica API to provide the user with the senators who have received the most
        amount of funding from a particular industry.

        As the function makes as many calls as there are senators in a particular sitting of Congress, it may take a
        while to return the necessary results.

        Parameters
        ----------
        propublica_api_key: class ProPublicaAPIKey
            The user's ProPublica API Key. See documentation on ProPublicaAPIKey.

        industry_id: str, optional
            Unique industry_id. Full list of industry IDs can be found at www.opensecrets.org/downloads/crp/CRP_IDs.xls.
            The user can also call top_20_industries_ids() to retrieve industry_ids. See documentation on
            top_20_industries_ids() (the default is 'H04', corresponding to Pharmaceuticals/Health Products industry).

        **kwargs : str, optional
            Extra arguments to 'propublica_api_key.senate_members'. See documentation on
            propublica_api_key.senate_members for possible arguments.

        Returns
        -------
        pandas.DataFrame
            Pandas DataFrame with Senators ranked according to who has received the most amount of funding from a
            particular industry.

        Examples
        --------
        >>> OpenSecrets = OpenSecretsAPIKey('insert OpenSecrets API Key here')
        >>> ProPublica = ProPublicaAPIKey('insert ProPublica API Key here')
        >>> OpenSecrets.top_senators_each_industry(ProPublica, industry_id = 'F09', congress_sitting = 116)
        [   cand_name	        cid	        cycle	industry	last_updated	party	state	        total
        0	Casey, Bob	        N00027503	2018	Insurance	06/10/19	    D	    Pennsylvania	357820.0
        1	Scott, Rick	        N00043290	2018	Insurance	06/10/19	    R	    Florida	        328912.0
        2	Brown, Sherrod	    N00003535	2018	Insurance	06/10/19	    D	    Ohio	        316800.0
        3	McSally, Martha	    N00033982	2018	Insurance	06/10/19	    R	    Arizona	        294825.0
        4	Stabenow, Debbie	N00004118	2018	Insurance	06/10/19	    D	    Michigan	    292400.0
        ...	...	                ...	        ...	    ...	        ...	            ...	    ...	            ...
        95	Boozman, John	    N00013873	2018	Insurance	06/10/19	    R	    Arkansas	    3450.0
        96	Lee, Mike	        N00031696	2018	Insurance	06/10/19	    R	    Utah	        3250.0
        97	Udall, Tom	        N00006561	2018	Insurance	06/10/19	    D	    New Mexico	    1058.0
        98	Leahy, Patrick	    N00009918	2018	Insurance	06/10/19	    D	    Vermont	        1015.0
        99	Shelby, Richard C	N00009920	2018	Insurance	06/10/19	    R   	Alabama	        -5000.0
        100 rows × 8 columns    ]

        See Also
        --------
        top_20_industries_ids() : Extracts the Top 20 Industries that have spent the most on Federal Lobbying from
        https://www.opensecrets.org/federal-lobbying/industries.

        class ProPublicaAPIKey: All functions that require the ProPublica API Key.
        """
        # Extracting Senators' CRP_IDs
        senators_crp_id = propublica_api_key.senate_members(**kwargs)['crp_id']
        # Initialising empty DataFrame for storing results
        result = pd.DataFrame()
        # for loop to retrieve the contribution received by each senator from the industry and storing them in DataFrame
        for senator_id in senators_crp_id:
            params = {'apikey': self.opensecrets_api_key, 'cid': senator_id, 'ind': industry_id, 'output': 'json'}
            r_opensecrets = requests.get('https://www.opensecrets.org/api/?method=candIndByInd&', params=params)
            # Passing calls that may return a null result as record is non-existent
            try:
                r_json = r_opensecrets.json()
                r_df = pd.DataFrame(r_json['response']['candIndus'])
                r_df_transpose = r_df.transpose()
                # Progressively building DataFrame by adding each successful call to the DataFrame
                result = pd.concat([result, r_df_transpose])
            except JSONDecodeError:
                pass
        try:
            # Changing values in 'total' column from str to float for sorting later
            result['total'] = result['total'].astype(float)
            # Selecting relevant columns to return
            new_cols = ['cand_name', 'cid', 'cycle', 'industry', 'last_updated', 'party', 'state', 'total']
            result = result.sort_values('total', ascending=False)[new_cols]
            result = result.reset_index(drop=True)
            return result
        except KeyError:
            print(f'Error: Unexpected content returned from API. Check if API Key is correct.')

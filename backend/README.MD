# Implemented Endpoints


<details>
  <summary>CHAMPION-MASTERY-V4</summary>

  ```
    ✔️ /lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}
    ❌ /lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}/by-champion/{championId}
    ✔️ /lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}/top
    ✔️ /lol/champion-mastery/v4/scores/by-summoner/{encryptedSummonerId}
  ```

  ⚠️ If the summoner has no mastery on a champion, the endpoint will return a 404 error.
</details>


<details>
  <summary>CHAMPION-V3</summary>

  ```
    ✔️ /lol/platform/v3/champion-rotations
  ```
</details>


<details>
  <summary>MATCH-V5</summary>

  ```
    ✔️ /riot/account/v1/accounts/by-puuid/{puuid}
    ✔️ /lol/match/v5/matches/{matchId}
    ✔️ /lol/match/v5/matches/{matchId}/timeline
  ```
</details>


<details>
  <summary>SUMMONER-V4</summary>

  ```
    ✔️ /lol/summoner/v4/summoners/by-account/{encryptedAccountId}
    ✔️ /lol/summoner/v4/summoners/by-name/{summonerName}
    ✔️ /lol/summoner/v4/summoners/by-puuid/{encryptedPUUID}
    ✔️ /lol/summoner/v4/summoners/{encryptedSummonerId}
  ```
</details>

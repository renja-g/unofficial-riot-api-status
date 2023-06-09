# Implemented Endpoints


<details>
  <summary>CHAMPION-MASTERY-V4</summary>

  ```
    ✔️ /lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}
    ❌ /lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}/by-champion/{championId}
    ✔️ /lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}/top
    ✔️ /lol/champion-mastery/v4/scores/by-summoner/{encryptedSummonerId}

    ⚠️ If the summoner has no mastery on a champion, the endpoint will return a 404 error.
  ```
</details>


<details>
  <summary>CHAMPION-V3</summary>

  ```
    ✔️ /lol/platform/v3/champion-rotations
  ```
</details>


<details>
  <summary>LEAGUE-EXP-V4</summary>

  ```
    ✔️ /lol/league-exp/v4/entries/{queue}/{tier}/{division}
  ```
</details>


<details>
  <summary>LEAGUE-V4</summary>

  ```
    ✔️ /lol/league/v4/challengerleagues/by-queue/{queue}
    ✔️ /lol/league/v4/entries/by-summoner/{encryptedSummonerId}
    ✔️ /lol/league/v4/entries/{queue}/{tier}/{division}
    ✔️ /lol/league/v4/grandmasterleagues/by-queue/{queue}
    ✔️ /lol/league/v4/leagues/{leagueId}
    ✔️ /lol/league/v4/masterleagues/by-queue/{queue}
  ```
</details>


<details>
  <summary>LOL-CHALLENGES-V1</summary>

  ```
    ✔️ /lol/challenges/v1/challenges/config
    ✔️ /lol/challenges/v1/challenges/percentiles
    ✔️ /lol/challenges/v1/challenges/{challengeId}/config
    ✔️ /lol/challenges/v1/challenges/{challengeId}/leaderboards/by-level/{level}
    ✔️ /lol/challenges/v1/challenges/{challengeId}/percentiles
    ✔️ /lol/challenges/v1/player-data/{puuid}

    ⚠️ pbe1 is not supported
  ```
</details>


<details>
  <summary>LOL-STATUS-V4</summary>

  ```
    ✔️ /lol/status/v4/platform-data
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

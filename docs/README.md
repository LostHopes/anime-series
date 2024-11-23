# Functional requirements

List of requirements for interaction with the service and permissions.
Feel free to request your changes.

## Account

1. User can register account with Google, GitHub or directly through service.
2. User must have strong password (more than 8 characters, which includes digits and symbols. E.g. $, #, !, ?)
3. User must verify person through captcha
4. User can enable 2FA in the profile
5. User can decide whether to keep logged in the account
6. User can recover his password through email
7. User can delete his account permanently with all data (in case of attack or user decision the data will be stored on the server for 90 days)
8. User can change account privacy (private except friends, publicly available for anyone)
9. User can change the username (with interval of 30 days)

## Friends

1. User can request a friend with other users
2. User can cancel the request
3. User can accept, reject or ignore the request
4. User can delete the friend

## Anime

1. User can suggest changes for the anime
2. User can add, remove, update his collection of anime
3. User can sort anime
    - by rating
    - by date out (from ascent and descend)
4. User can filter the anime
    - by genre(-s)
    - by year
    - by season
    - by studio(-s)
    - by source (original or manga)
    - by country

## Discussions

1. User can create discussions if logged in
2. User can edit the message
3. User can reply to the message (create thread)
4. User can delete the message
5. Moderator/admin can close the discussion in case of rules violation

# Designing database schemas


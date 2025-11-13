# MCP Agent with AWS Strands:

Starting point: [strands-agents/samples](https://github.com/strands-agents/samples)

## Get Started

1. Setup virtual environment for Python \
    See instructions in [docs/venv.md](docs/venv.md)
2. Install AWS CLI:
    ```bash
    brew install awscli
    ```
    make sure you get v2 installed:
    ```bash
    > aws --version
    aws-cli/2.31.32 Python/3.13.9 Darwin/25.0.0 source/arm64
    ```
3. Configure AWS CLI for SSO:
    https://docs.aws.amazon.com/cli/latest/reference/configure/sso.html
    `~/.aws/config`:
    ```
    [default]
    region = us-east-1
    output = yaml

    [sso-session <SessionName>]
    sso_start_url = <your start URL, you can get from AWS access portal : https://<session>.awsapps.com/start/#/?tab=accounts>
    sso_registration_scopes = sso:account:access
    sso_region = us-east-1

    [profile <profile name>]
    sso_session = <SessionName>
    sso_account_id = <account id you can get from AWS access portal : https://<session>.awsapps.com/start/#/?tab=accounts>
    sso_role_name = <Role Name you can get from AWS access portal : https://<session>.awsapps.com/start/#/?tab=accounts>
    region = us-east-1
    ```
    __Note__: `<session>` is customer specific, would identify AWS customer name.
    read more here: [How IAM Identity Center authentication is resolved for AWS SDKs and tools](https://docs.aws.amazon.com/sdkref/latest/guide/understanding-sso.html)
4. Create `.env` file and put necessary AWS env vars in it, 
    authenticate with aws sso
    see [.env.example](.env.example)

5. Run prototype
    ```bash
    python main.py
    ```

## How to pick model with permissions to use: 

1. go to [AWS Console](https://us-east-1.console.aws.amazon.com/console/home?region=us-east-1) \
    in my case (Pavlo Filkovskyi) with SSO login i had to navigate to `AWS access portal` first: \
    `https://<session>.awsapps.com/start/#/?tab=accounts`, \
    where `<session>` - is customer specific, usually customer's name. \
    then i picked necessary account from the list appeared on the screen and clicked on it, \
    it would uncollapsed into 2 links looking like: `<account role> | Access Keys` \
    `<account role>` link took me to the console page
2. At the console page use search bar at the top left, and search for `Amazon Bedrock`
3. When found, open it and scroll slightly down, see the `Test` section, (Chat / Text playground)
4. click `Open playground` and you'll see button on the top left of the chat - `Select Model`
5. click `Select Model` and brows categories and models, seee which ones you have access to.
6. pick one, click `Apply`
7. in chat window, top left see `Configuration` section with the model name and (i) icon next to it - clic on it, then in a popup click `View Details`
8. Model's details will open in a new tab, scroll a bit down to see `Model ID` - that's what you need!

## Troubleshooting in local env:

If running `main.py` crashes with exception saying `Your AWS Token has expired`, 
this might be caused by the fact that python venv somehow picks up variables it not supposed to pick: 
`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`. 
Even if just freshly updated from AWS Access Portal these local env vars appear not to be working as expected.

Workaround: 
```bash
unset AWS_ACCESS_KEY_ID && unset AWS_SECRET_ACCESS_KEY && unset AWS_SESSION_TOKEN
```
Then make sure you have authenticated with SSO and rerun `main.py`

## References:
- https://github.com/strands-agents/sdk-python
- https://github.com/strands-agents/samples
- https://github.com/strands-agents/tools
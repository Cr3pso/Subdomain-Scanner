# Subdomain-Scanner
This tool is a simple script made with python, which makes a brute-force attack trying to guess the subdomains of a server.

## How to install the tool?
```
git clone https://github.com/Cr3pso/Subdomain-Scanner
```

```
pip install -r requirements.txt
```

## How to use the tool?
### - If we type **python3 subdomain-scanner.py** we can see that we need to write some parameters

### Let's see which parameters can we use:
```
python3 subdomain-scanner.py -h
```
**[t/--target]** To indicate victim's domain")

**[-w/--wordlist]** To indicate the subdomain's wordlist")

**[-http/--http]** For only sending HTTP requests (Default http & https)")

**[-https/--https]** For only sending HTTPS requests (Default http & https)

#
## Example:
```
python3 subdomain-scanner.py -t thisisatest.com -w /usr/share/wordlists/wordlists.txt -https
```


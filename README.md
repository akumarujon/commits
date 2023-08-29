# Fake commits

#### To increase amount of commits.

### Clone this repository
```bash
git clone https://github.com/akumarujon/commits
```
and
```bash
cd commits
```

Remove remote:
```bash
git remote remove origin
```
add your github repo
```bash
git remote add origin https://github.com/USERNAME/REPO
```

#### Run the script

<details>
<summary>Python</summary>

> You can change the number of commits on `main.py`
```bash
python main.py
```

</details>

<details>
<summary>Rust</summary>

> You can change the number of commits on `flood.rs`

Compile:
```bash
rustc flood.rs
```
Run:
```bash
./flood
```

</details>

If you are using vscode, it asks to log in your github account.

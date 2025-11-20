# Cheat Sheet: Kontrollstrukturen

Schnellreferenz für if/elif/else und Schleifen.

## if/elif/else

### Einfache Bedingung

```python
if bedingung:

    # Code wenn True

```text

### if-else

```python
if bedingung:

    # Code wenn True

else:

    # Code wenn False

```text

### if-elif-else

```python
if bedingung1:

    # Code wenn bedingung1 True

elif bedingung2:

    # Code wenn bedingung2 True

else:

    # Code wenn alle False

```text

### Ternärer Operator

```python
wert = a if bedingung else b
```text

## for-Schleifen

### Über Liste

```python
for item in liste:
    print(item)
```text

### Mit range()

```python
for i in range(10):      # 0-9
    print(i)

for i in range(1, 11):   # 1-10
    print(i)

for i in range(0, 10, 2): # 0,2,4,6,8
    print(i)
```text

### Mit enumerate()

```python
for index, item in enumerate(liste):
    print(f"{index}: {item}")
```text

### Über Dictionary

```python
for key in dict:
    print(key)

for key, value in dict.items():
    print(f"{key}: {value}")
```text

## while-Schleifen

### Grundform

```python
while bedingung:

    # Code

```text

### Mit Zähler

```python
i = 0
while i < 10:
    print(i)
    i += 1
```text

### Endlosschleife

```python
while True:
    if bedingung:
        break
```text

## Schleifensteuerung

### break

```python
for i in range(10):
    if i == 5:
        break  # Stoppt Schleife
```text

### continue

```python
for i in range(10):
    if i % 2 == 0:
        continue  # Überspringt Rest
    print(i)
```text

### pass

```python
for i in range(10):
    if i == 5:
        pass  # Macht nichts
    else:
        print(i)
```text

## Häufige Patterns

### Zählen

```python
count = 0
for item in liste:
    if bedingung:
        count += 1
```text

### Filtern

```python
ergebnis = []
for item in liste:
    if bedingung:
        ergebnis.append(item)
```text

### Summieren

```python
total = 0
for zahl in zahlen:
    total += zahl
```text

---

**Zurück zu:** [Materialien README](./README.md)

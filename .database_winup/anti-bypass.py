def calling (value):
  table = value.split(".")
  encodeforing = "COPY.CODEDATE.ONLINE-MODE"
  if table[0] == 2:
    encodeforing.replace("CODEDATE", "1-CODEDATE2")
  if table[1] == 5:
    encodeforing.replace("CODEDATE2", "0-DATA3")
  encodeforing.replace("DATA3", "0")
  return encodeforing

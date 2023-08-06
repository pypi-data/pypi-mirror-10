elefant
---

Allows you to backup and restore your Heroku database
using your own private storage in S3. This allow circumventing
the backup limit in Heroku plans and also gives peace of mind 
that your data is backed up somewhere else besides Heroku.

Tested on Postgres 9.4.

Usage: 

* Ensure AWS credentials are set up in environment variables
* Ensure heroku is logged in with $ heroku login 

## Example 

```python
from elefant import Elefant


# create Elefant object, passing in the Heroku app name
hb = Elefant("myapp")

print "Making and backup and uploading to S3..."
hb.backup() 

print "Availiable backups:"
backups = hb.backups 
for b in backups: 
	print b.name

print "Restoring from most recent backup..."
hb.restore(b) 

print "Restoring from most recent backup using a string..."
hb.restore(b.name)
```
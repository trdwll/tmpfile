import os, hashlib


# Could probably do this via md5sum and sha1sum, but whatever
def get_checksums(file):
	hash_sha1 = hashlib.sha1()
	hash_sha256 = hashlib.sha256()
	hash_sha512 = hashlib.sha512()

	with open(file, 'rb') as f:
		for chk in iter(lambda: f.read(4096), b""):
			hash_sha1.update(chk)
			hash_sha256.update(chk)
			hash_sha512.update(chk)

	return [hash_sha1.hexdigest(), hash_sha256.hexdigest(), hash_sha512.hexdigest()]
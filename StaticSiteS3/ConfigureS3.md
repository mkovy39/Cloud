## Step 1: Create an S3 Bucket

1. Go to the AWS S3 Console.
2. Click "Create bucket".
3. Name your bucket exactly as your domain (e.g., `mkovy.com`).
4. Uncheck "Block all public access".
5. Enable static website hosting under the Properties tab.
6. Set:
   - Index document: `index.html`
   - Error document (optional): `error.html`
7. Save settings and note the bucket website endpoint.

---

## Step 2: Upload Website Files

1. Prepare your website files (`index.html`, `style.css`, etc.).
2. Upload the files to your S3 bucket.
3. Ensure the `index.html` file is at the root level of your bucket.

---

## Step 3: Set Permissions for Public Access

### Bucket Policy

1. Go to the Permissions tab of your S3 bucket.
2. Scroll to "Bucket policy", click Edit, and paste the following:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```

Replace `your-bucket-name` with the actual name of your bucket.

3. Save the policy.
4. Your website is now publicly accessible via the S3 website endpoint.

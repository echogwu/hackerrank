class Solution:

    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        emails = set(emails)
        result = set()
        for email in emails:
            domain = email[email.find("@") + 1:]
            localname = email[:email.find("@")]
            if localname.find("+") != -1:
                localname = localname[:localname.find("+")]
                localname = localname.replace(".", "")
            email = localname + "@" + domain
            if email not in result:
                result.add(email)
        return len(result)


s = Solution()
emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
print(s.numUniqueEmails(emails))

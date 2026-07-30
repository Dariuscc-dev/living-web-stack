import uuid

class Contact:
    def __init__(self, name, role, company, linkedin_url, status="Lead", contact_id=None):
        # Generates a unique short ID if one doesn't exist
        self.id = contact_id if contact_id else str(uuid.uuid4())[:6]
        self.name = name
        self.role = role
        self.company = company
        self.linkedin_url = linkedin_url
        self.status = status

    def to_dict(self):
        """Converts the object into a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "company": self.company,
            "linkedin_url": self.linkedin_url,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Contact object from a dictionary."""
        return cls(
            name=data["name"],
            role=data["role"],
            company=data["company"],
            linkedin_url=data.get("linkedin_url", "N/A"),
            status=data.get("status", "Lead"),
            contact_id=data["id"]
        )

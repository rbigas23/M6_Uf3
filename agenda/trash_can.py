# Estos son __repr__ que ya no hacen falta:

# def __repr__(self):
#     return f"agenda(events=[{', '.join([repr(event) for event in self.events])}], users=[{', '.join(repr(user) for user in self.user_ids)}])"

# def __repr__(self):
#     return f"user(id={repr(self.id)}, name={repr(self.name)})"

# def __repr__(self):
#     return f"event(date={repr(self.date)}, duration={repr(self.duration)}, title={repr(self.title)}, description={repr(self.description)}, tags={repr(self.tags)}, location={repr(self.location)})"

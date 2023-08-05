import vs


class Room:

	def __init__(self, handle):
		self.handle = handle
		self.raumnummer = vs.GetRField(self.handle, "DB_SPACE", "SpaceNumber")


class Floor:
	def __init__(self, handle):
		self.handle = handle
		self.bounding_space = None
		self.components = {}

	def get_components(self):
		nums = vs.GetNumberOfComponents(self.handle)
		for i in range(nums[1] + 1):
			name = vs.GetComponentName(self.handle, i)
			height = vs.GetComponentWidth(self.handle, i)
			self.components[name] = height[1]

		self.components.pop("")

		return self.components

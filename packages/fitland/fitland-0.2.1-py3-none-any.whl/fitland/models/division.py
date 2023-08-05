from pymongoose.mongo_types import Types, Schema

class Division (Schema):
	schema_name = "divisions"

	id = None
	name = None
	description = None
	sold = None
	category = None
	n_athletes = None

	def __init__ (self, **kwargs):
		self.schema = {
			"competition": {
				"type": Types.ObjectId,
				"ref": "competitions",
				"required": True
			},
			"name": {
				"type": Types.String,
				"required": True
			},
			"description": {
				"type": Types.String,
				"required": True
			},
			
			"category": {
				"type": Types.Number,
				"default": 0,
				"required": True
			},
			
			"n_athletes": {
				"type": Types.Number,
				"required": True
			},
			"gender": {
				
				"n_persons_a": {
					"type": Types.Number,
					"default": 0
				},
				
				"n_persons_b": {
					"type": Types.Number,
					"default": 0
				},
				"free": {
					"type": Types.Number,
					"default": 0
				},
				
			},
			"minimum_age": {
				"type": Types.Number,
				"default": 18
			},
			# TODO:
			"benchmark": {
				# "name": {
				# 	"type": Types.String,
				# },
				# "b_type": {
				# 	"type": Types.Number
				# },
				# "ranking": {
				# 	"type": Types.Number,
				# },
				# "collect": {
				# 	"type": Types.Boolean,
				# 	"default": False
				# }
			},
			"waiver": {
				# "type": Types.Boolean,
				# "default": False
			},
			"color": {
				"type": Types.String,
				"default": "ffffffff"
			}
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def __str__ (self):
		return f"Division: {self.id} - {self.name}"

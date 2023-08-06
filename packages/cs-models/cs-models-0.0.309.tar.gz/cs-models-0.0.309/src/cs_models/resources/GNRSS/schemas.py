from marshmallow import (
    Schema,
    fields,
    validate,
)


class GNRSSResourceSchema(Schema):
    not_blank = validate.Length(min=1, error='Field cannot be blank')

    id = fields.Integer(dump_only=True)
    article_id = fields.Integer(required=True)
    article_date = fields.DateTime(required=True)
    updated_at = fields.DateTime()

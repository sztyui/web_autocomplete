from webapp import ma

class VarosSchema(ma.Schema):
    class Meta:
        fields = ('nev', 'típus', 'megye', 'kisterseg', 'nepesseg', 'iranyitoszam',)

city_schema = VarosSchema()
cities_schema = VarosSchema(many=True)


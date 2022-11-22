from django.contrib import admin
from cargo_app.models import TraderModel,PricingMethodeModel,StrategyModel,PhysicalBlotter,HolidayModel,CounterPartyModel,BookModel,ProductModel,PricingContractModel,UnitModel
from cargo_app.models import DerivativeModel,TypeModel,BrockersModel,ClearerModel,ClearerRatesModel,BrokerageModel

# Register your models here.

admin.site.register(TraderModel)
admin.site.register(PricingMethodeModel)
admin.site.register(StrategyModel)
admin.site.register(PhysicalBlotter)
admin.site.register(HolidayModel)
admin.site.register(CounterPartyModel)
admin.site.register(BookModel)
admin.site.register(ProductModel)
admin.site.register(PricingContractModel)
admin.site.register(UnitModel)

admin.site.register(DerivativeModel)
admin.site.register(TypeModel)
admin.site.register(BrockersModel)
admin.site.register(ClearerModel)
admin.site.register(ClearerRatesModel)
admin.site.register(BrokerageModel)
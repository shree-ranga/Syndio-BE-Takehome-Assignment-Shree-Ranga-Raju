from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from mathapp.models import Employees
from mathapp.helper import calc_protected_class_pvalue


class GetPValue(APIView):
    def get(self, request, *args, **kwargs):
        department = request.query_params.get("department", None)
        if not department:
            return Response(
                {"error": "Please specify department as a query param."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        valid_departments = {"Engineering"}
        if department not in valid_departments:
            return Response(
                {
                    "error": f"Invalid department: '{department}'. Must be one of: {', '.join(valid_departments)}."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Filter the data for the specified department
        query = Employees.objects.filter(department=department)
        data = list(query.values())
        pvalue = calc_protected_class_pvalue(data=data)
        return Response({"pvalue": round(pvalue, 3)}, status=status.HTTP_200_OK)

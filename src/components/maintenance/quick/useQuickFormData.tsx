
import { useState, useEffect } from 'react';
import { MaintenanceRequest, BranchData, ServiceTypeData } from '@/types/maintenance';
import { supabase } from '@/integrations/supabase/client';
import { toast } from "@/components/ui/use-toast";

export const useQuickFormData = () => {
  const [isLoading, setIsLoading] = useState(true);
  const [branches, setBranches] = useState<BranchData[]>([]);
  const [serviceTypes, setServiceTypes] = useState<ServiceTypeData[]>([]);
  const [formData, setFormData] = useState<MaintenanceRequest>({
    branch: '',
    serviceType: '',
    title: '',
    description: '',
    priority: 'medium',
    requestedDate: new Date().toISOString().split('T')[0],
    estimatedCost: '',
    attachments: []
  });

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);
      try {
        const { data: storesData, error: storesError } = await supabase
          .from('stores')
          .select('id, name')
          .eq('is_deleted', false);
        
        if (storesError) throw storesError;
        
        const { data: servicesData, error: servicesError } = await supabase
          .from('maintenance_services')
          .select('id, name, description')
          .eq('is_active', true)
          .eq('is_deleted', false);
        
        if (servicesError) throw servicesError;
        
        setBranches(storesData || []);
        setServiceTypes(servicesData || []);

        console.log('تم تحميل البيانات بنجاح:', { 
          branches: storesData?.length, 
          services: servicesData?.length 
        });
      } catch (error) {
        console.error('خطأ في جلب البيانات:', error);
        toast({
          title: "خطأ في تحميل البيانات",
          description: "سيتم استخدام البيانات الافتراضية",
          variant: "destructive",
        });
        
        setBranches([
          { id: "1", name: "الرياض" },
          { id: "2", name: "جدة" },
          { id: "3", name: "مكة" },
          { id: "4", name: "المدينة" },
          { id: "5", name: "الدمام" },
          { id: "6", name: "الخبر" }
        ]);
        
        setServiceTypes([
          { id: "1", name: "صيانة عامة" },
          { id: "2", name: "صيانة كهربائية" },
          { id: "3", name: "صيانة سباكة" },
          { id: "4", name: "صيانة تكييف" },
          { id: "5", name: "صيانة أجهزة" },
          { id: "6", name: "أخرى" }
        ]);
      } finally {
        setIsLoading(false);
      }
    };
    
    fetchData();
  }, []);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };
  
  const handleSelectChange = (field: string, value: string) => {
    setFormData({
      ...formData,
      [field]: value
    });
  };
  
  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      const filesArray = Array.from(e.target.files);
      setFormData({
        ...formData,
        attachments: filesArray
      });
    }
  };

  const resetForm = () => {
    setFormData({
      branch: '',
      serviceType: '',
      title: '',
      description: '',
      priority: 'medium',
      requestedDate: new Date().toISOString().split('T')[0],
      estimatedCost: '',
      attachments: []
    });
  };

  return {
    isLoading,
    branches,
    serviceTypes,
    formData,
    handleChange,
    handleSelectChange,
    handleFileChange,
    resetForm
  };
};

export interface User {
  id: number;
  username: string;
  email: string;
  role: 'USER' | 'SECURITY_ANALYST' | 'ADMIN';
  department?: string;
  is_active_employee: boolean;
  first_name: string;
  last_name: string;
}

export interface SecurityEvent {
  id: number;
  user_name?: string;
  event_type: string;
  timestamp: string;
  description: string;
  severity: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
  source: string;
  status: string;
  risk_score: number;
  ip_address?: string;
  device_info?: string;
  location?: string;
  metadata?: Record<string, any>;
}

export interface Threat {
  id: number;
  category: string;
  user_name?: string;
  severity: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
  status: 'OPEN' | 'INVESTIGATING' | 'RESOLVED' | 'FALSE_POSITIVE';
  description: string;
  created_at: string;
  resolved_at?: string;
}

export interface Alert {
  id: number;
  user_name?: string;
  severity: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
  risk_score: number;
  message: string;
  status: 'NEW' | 'ACKNOWLEDGED' | 'INVESTIGATING' | 'RESOLVED' | 'DISMISSED';
  created_at: string;
  resolved_at?: string;
}

export interface Incident {
  id: number;
  title: string;
  description: string;
  severity: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
  status: 'OPEN' | 'INVESTIGATING' | 'CONTAINED' | 'RESOLVED' | 'CLOSED';
  assigned_to_name?: string;
  created_at: string;
}

export interface DashboardStats {
  total_events: number;
  total_threats: number;
  total_alerts: number;
  recent_events: number;
}
